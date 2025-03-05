name = "pbcore_full_v1"
body = {
    "settings": {
        "analysis": {
            "analyzer": {
                "my_analyzer": {
                    "type": "custom",
                    "tokenizer": "standard",
                    "filter": ["lowercase", "asciifolding"]
                }
            }
        }
    },
    "mappings": {
        "properties": {
            "pbcoreDescriptionDocument": {
            "type": "nested",
            "properties": {
                "xsi:schemaLocation": { "type": "keyword" },
                "pbcoreAssetType": { "type": "keyword" },
                "pbcoreAssetDate": {
                    "type": "nested",
                    "properties": {
                        "dateType": { "type": "keyword" },
                        "text": { "type": "date" }
                    }
                },
                "pbcoreIdentifier": {
                    "type": "nested",
                    "properties": {
                        "source": { "type": "keyword" },
                        "text": { "type": "keyword" }
                    }
                },
                "pbcoreTitle": {
                    "type": "nested",
                    "properties": {
                        "source": { "type": "keyword" },
                        "titleType": { "type": "keyword" },
                        "text": { "type": "text" }
                    }
                },
                "pbcoreSubject": {
                    "type": "keyword"
                },
                "pbcoreDescription": {
                    "type": "nested",
                    "properties": {
                        "source": { "type": "keyword" },
                        "descriptionType": { "type": "keyword" },
                        "text": { "type": "text" }
                    }
                },
                "pbcoreGenre": {
                    "type": "nested",
                    "properties": {
                        "source": { "type": "keyword" },
                        "annotation": { "type": "keyword" },
                        "text": { "type": "keyword" }
                    }
                },
                "pbcoreCreator": {
                    "type": "nested",
                    "properties": {
                        "creator": { "type": "text" },
                        "creatorRole": { "type": "keyword" }
                    }
                },
                "pbcoreContributor": {
                    "type": "nested",
                    "properties": {
                        "contributor": { "type": "text" },
                        "contributorRole": { "type": "keyword" }
                    }
                },
                "pbcoreRightsSummary": { "type": "text" },
                "pbcoreInstantiation": {
                    "type": "nested",
                    "properties": {
                        "instantiationIdentifier": {
                            "type": "nested",
                            "properties": {
                                "source": { "type": "keyword" },
                                "text": { "type": "keyword" }
                            }
                        },
                        "instantiationPhysical": { "type": "keyword" },
                        "instantiationLocation": { "type": "keyword" },
                        "instantiationMediaType": { "type": "keyword" },
                        "instantiationGenerations": { "type": "keyword" },
                        "instantiationDuration": { "type": "text" },
                        "instantiationAnnotation": {
                            "type": "nested",
                            "properties": {
                                "annotationType": { "type": "keyword" },
                                "text": { "type": "text" }
                            }
                        },
                        "instantiationDate": {
                            "type": "nested",
                            "properties": {
                                "instantiationDate": { "type": "date" }
                            }
                        },
                        "instantiationFileSize": { "type": "keyword" },
                        "instantiationTracks": { "type": "keyword" },
                        "instantiationEssenceTrack": {
                            "type": "nested",
                            "properties": {
                                "essenceTrackType": { "type": "keyword" },
                                "essenceTrackIdentifier": { "type": "keyword" },
                                "essenceTrackEncoding": { "type": "keyword" },
                                "essenceTrackDataRate": {
                                    "type": "nested",
                                    "properties": {
                                        "unitsOfMeasure": { "type": "keyword" },
                                        "text": { "type": "text" }
                                    }
                                },
                                "essenceTrackDuration": { "type": "text" },
                                "essenceTrackAnnotation": {
                                    "type": "nested",
                                    "properties": {
                                        "essenceTrackAnnotation": { "type": "text" }
                                    }
                                }
                            }
                        }
                    }
                },
                "pbcoreAnnotation": {
                    "type": "nested",
                    "properties": {
                        "annotationType": { "type": "keyword" },
                        "text": { "type": "text" }
                    }
                }
            }
            }
        }
    }
}