#!/usr/bin/env python3

import argparse
import sys
from typing import Any, Dict
import requests
import os
from mysecrets import *

import pinecone 

SEARCH_TOP_K = 3
destination_files_dir="destFilesDir"

#cli help
parser = argparse.ArgumentParser(
                    prog='VectorDB Utils',
                    description=f'Vector DB API to post file from {destination_files_dir}, post prompt, get embeddings')

args = parser.parse_args()
print()

for c,arg in enumerate(sys.argv):
	if c==1:
		source_fname = arg
		print("Text SOURCE file: " + source_fname)

def upsert_file(directory: str):
    """
    Upload all files under a directory to the vector database.
    """
    url = "http://0.0.0.0:8000/upsert-file"
    headers = {"Authorization": "Bearer " + DATABASE_INTERFACE_BEARER_TOKEN}
    files = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_path = os.path.join(directory, filename)
            with open(file_path, "rb") as f:
                file_content = f.read()
                files.append(("file", (filename, file_content, "text/plain")))
            response = requests.post(url,
                                     headers=headers,
                                     files=files,
                                     timeout=600)
            if response.status_code == 200:
                print(filename + " uploaded successfully to vector db.")
            else:
                print(
                    f"Error: {response.status_code} {response.content} for uploading "
                    + filename)

def upsert(id: str, content: str):
    """
    Upload one piece of text to the database.
    """
    url = "http://0.0.0.0:8000/upsert"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + DATABASE_INTERFACE_BEARER_TOKEN,
    }

    data = {
        "documents": [{
            "id": id,
            "text": content,
        }]
    }
    response = requests.post(url, json=data, headers=headers, timeout=600)

    if response.status_code == 200:
        print("uploaded successfully.")
    else:
        print(f"Error: {response.status_code} {response.content}")

def query_database(query_prompt: str) -> Dict[str, Any]:
    """
    Query vector database to retrieve chunk with user's input question.
    """
    url = "http://0.0.0.0:8000/query"
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json",
        "Authorization": f"Bearer {DATABASE_INTERFACE_BEARER_TOKEN}",
    }
    data = {"queries": [{"query": query_prompt, "top_k": SEARCH_TOP_K}]}

    response = requests.post(url, json=data, headers=headers, timeout=600)

    if response.status_code == 200:
        result = response.json()
        # process the result
        return result
    else:
        raise ValueError(f"Error: {response.status_code} : {response.content}")

def delete_all_vecs():  
    pinecone.init(api_key=PINECONE_API_KEY, environment='gcp-starter') 
    index = pinecone.Index('gpt-with-embeddings') 
    #query = index.query(queries=[], include_ids=True, top_k=1000)  # Set a sufficient top_k value
    res = index.query(vector=[0 for _ in range(1536)], top_k=10000)
    #print("HERE:",res)
    # Retrieve all keys from the query results
    for match in res['matches']:
         print(match.id)
         delete_response = index.delete(ids=[match.id])
         print("Delete response:",delete_response)

if __name__ == "__main__":
    print("\033[43mUpload Page Chunks.\033[0m")
    upsert_file(destination_files_dir)
    #delete_all_vecs()