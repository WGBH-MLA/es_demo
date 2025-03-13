# Bill moyers collection link

# from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import requests


def download_from_search_url(search_url, fetch_transcripts=True):
    # Fetch the search results; bail on fail
    search_response = requests.get(search_url)
    if search_response.status_code != 200:
        print(f"Failed to fetch data: {search_response.status_code}")
        exit()

    data = search_response.json()

    # Bail if no documents
    if len(data['response']['docs']) == 0:
        print("No documents found.")
        exit()

    # Grab the IDs
    ids = [doc['id'] for doc in data['response']['docs']]

    print(f"Fetching {len(ids)} PBCore JSON documents...")

    for id in ids:
        pbcore_url = f"https://americanarchive.org/api/{id}.json"
        print(f"Fetching PBCore JSON for {id}...")
        pbcore_response = requests.get(pbcore_url)

        # Skip if not 200
        if pbcore_response.status_code != 200:
            print(f"Failed to fetch PBCore JSON for {id}: {pbcore_response.status_code}")
            continue

        # Write the PBCore JSON to a file named with the ID.
        print(f"Writing PBCore JSON for {id} to data/pbore_json/{id}.txt ...")
        with open(f"data/pbcore_json/{id}.json", "w") as f:
            json.dump(pbcore_response.json(), f, indent=4)

        if fetch_transcripts:        
            # Fetch the transcript
            transcript_url = f"https://americanarchive.org/transcripts/{id}"
            print(f"Fetching Transcript for {id}...")
            transcript_response = requests.get(transcript_url)
            if transcript_response.status_code != 200:
                print(f"Failed to fetch transcript for {id}: {transcript_response.status_code}")
                continue

            # Write the transcript to a file named with the ID.
            print(f"Writing Transcript for {id} to data/transcripts/{id}.txt ...")
            with open(f"data/transcripts/{id}.txt", "w") as f:
                # Use BeautifulSoup to parse the HTML content
                soup = BeautifulSoup(transcript_response.content, "html.parser")
                # Extract text (removing script and style content)
                text = soup.get_text(separator="\n", strip=True)
                f.write(text)



if __name__ == "__main__":
    search_urls = [
        "https://americanarchive.org/catalog.json?f[access_types][]=online&f[special_collections][]=bill-moyers&page=8&per_page=100&sort=asset_date+asc",
        "https://americanarchive.org/catalog.json?utf8=%E2%9C%93&f%5Bseries_titles%5D%5B%5D=PBS+NewsHour&f%5Baccess_types%5D%5B%5D=all&q=tariffs&per_page=100",
        "https://americanarchive.org/catalog.json?f[access_types][]=all&f[series_titles][]=The+First+Amendment&page=2&per_page=100",
        "https://americanarchive.org/catalog.json?utf8=%E2%9C%93&f[series_titles][]=We+the+People&f[access_types][]=all&q=tariffs&per_page=100",
        "https://americanarchive.org/catalog.json?utf8=%E2%9C%93&f[series_titles][]=PBS+NewsHour&f[access_types][]=all&q=tariffs&per_page=100"
    ]

    for search_url in search_urls:
        print(f"Processing search URL: {search_url}")
        download_from_search_url(search_url, fetch_transcripts=False)