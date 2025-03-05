import os
from elasticsearch import Elasticsearch

api_key = os.environ.get("ES_API_KEY")
host = os.environ.get("ES_HOST")
client = Elasticsearch(host, api_key=api_key, verify_certs=False)