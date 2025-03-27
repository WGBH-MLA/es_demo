query_str = "Washington"

query_str_fields = [
    "pbcoreDescriptionDocument.pbcoreDescription.text",
    "pbcoreDescriptionDocument.pbcoreTitle.text"
]

query = {
    "query": {
        "bool": {
            "should": [
                {
                    "nested": {
                        "path": "pbcoreDescriptionDocument.pbcoreTitle",
                        "query": {
                            "match": {
                                "pbcoreDescriptionDocument.pbcoreTitle.text": query_str
                            }
                        }
                    }
                },
                {
                    "nested": {
                        "path": "pbcoreDescriptionDocument.pbcoreDescription",
                        "query": {
                            "match": {
                                "pbcoreDescriptionDocument.pbcoreDescription.text": query_str
                            }
                        }
                    }
                }
            ],
            "minimum_should_match": 1  # At least one match is required
        }
    }
}



def run_query():
    from demo.es import client
    resp = client.search(index="pbcore_full_v1", body=query)
    print(f"Total hits: {resp['hits']['total']['value']}")
    for hit in resp["hits"]["hits"]:
        print(hit["_id"])
        print(hit["_source"]["pbcoreDescriptionDocument"]["pbcoreTitle"][0]["text"])
        print(hit["_source"]["pbcoreDescriptionDocument"]["pbcoreDescription"][0]["text"])
    return resp
