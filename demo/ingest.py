import json
import os
from elasticsearch import helpers
from glob import glob
from pprint import pprint as pp

# import local modules
from demo import es
from demo.indices import pbcore_full_v1


def aapb_id_from_pbcore_doc(pbcore_doc):
    """
    Extracts pbcoreIdentifier where source="http://americanarchiveinventory.org".
    Returns None if not found.
    """
    try:
        return [x for x in pbcore_doc["pbcoreDescriptionDocument"]["pbcoreIdentifier"] if x['source'] == 'http://americanarchiveinventory.org' ][0]['text']
    except KeyError:
        return None

# Generator function to yield PBCore JSON documents from filenames.
def pbcore_docs(filenames):
    for filename in filenames:
        if not filename.endswith(".json"):
            print(f"Skipping non-JSON file: {filename}")
            continue
        with open(filename, "r", encoding="utf-8") as pbcore_json:
            try:
                pbcore = json.load(pbcore_json)
                yield pbcore
            except json.JSONDecodeError:
                print(f"Skipping invalid JSON file: {filename}")
                continue


# Generator function to yield PBCore JSON documents with metadata for bulk ingestion.
def pbocre_docs_bulk(pbcore_docs):
    """Yield PBCore JSON documents with metadata from files in the specified directory."""
    for pbcore_doc in pbcore_docs:
        aapb_id = aapb_id_from_pbcore_doc(pbcore_doc)
        if not aapb_id:
            print(f"Skipping file: No valid AAPB ID found.")
            continue
        # Put the PBCore doc under _source with additional metadata
        yield {
            "_index": index_name,
            "_id": aapb_id,
            "_op_type": "index",
            "_source": pbcore_doc
        }


def ingest(file_pattern, index_name):
    """Ingest a single PBCore JSON file into the specified Elasticsearch index."""
    filenames = glob(file_pattern)
    docs = list(pbcore_docs(filenames))

    if not docs:
        print(f"No pbcore JSON documents found for file pattern {file_pattern}")
        return
    elif len(docs) == 1:
        pbcore = docs[0]
        aapb_id = aapb_id_from_pbcore_doc(pbcore)
        es.client.index(index=index_name, id=aapb_id, document=pbcore)
        print(f"Ingested doc matching {file_pattern} with ID {aapb_id} into {index_name}")
    else:
        helpers.bulk(es.client, pbcore_docs_bulk(docs, index_name))
        print(f"Ingested {len(docs)} docs from file pattern {file_pattern} into {index_name}")


if __name__ == "__main__":
    try:
        es.client.indices.create(index=pbcore_full_v1.name, body=pbcore_full_v1.body)
        # ingest('data/1.json', 'pbcore_full_v1')

    except Exception as e:
        print(f"Error: {e}")