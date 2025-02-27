# es_demo - Elasticsearch and Kibana Demo Project
Get an Elasticsearch and Kibana instance deployed to EKS and play around with it.

## Goals
1. Learn and demonstrate K8s cluster creation suitable for production Elasticsearch instance for GBH Archives.
1. Learn and deploy Elasticsearch with Kibana to EKS cluster.
1. Ingest PBCore JSON documents
   1. Using `_bulk` API
      1. Gather performance results
      1. Test upper limits
   1. With schema autodetect
   1. With defined schema
   1. Compare strategies for indexing and querying hierarchical metadata (PBCore)
1. Ingest Transcripts
   1. Using `_bulk` API
      1. Gather performance results
      1. Test upper limits
   1. Semantic search
