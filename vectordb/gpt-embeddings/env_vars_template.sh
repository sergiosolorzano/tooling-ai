#!/bin/bash
#Azure Openai settings:https://github.com/openai/chatgpt-retrieval-plugin/blob/main/services/openai.py
export DATASTORE=pinecone
export BEARER_TOKEN="enter key"
export OPENAI_API_KEY="enter key"
export PINECONE_API_KEY="enter key"
export PINECONE_ENVIRONMENT="enter name"
export PINECONE_INDEX="enter name"

#Azure openai
#See references: https://github.com/openai/chatgpt-retrieval-plugin/blob/main/services/openai.py
#export OPENAI_EMBEDDINGMODEL_DEPLOYMENTID="enter name"
#export OPENAI_API_KEY="enter key"
#export AZURE_OPENAI_API_KEY="enter key"
#export OPENAI_API_BASE=https://<yourdomain>.openai.azure.com/
#export OPENAI_API_TYPE=azure
#export OPENAI_METADATA_EXTRACTIONMODEL_DEPLOYMENTID=<Name of deployment of model for metatdata>
#export OPENAI_COMPLETIONMODEL_DEPLOYMENTID=<Name of general model deployment used for completion>
#export OPENAI_EMBEDDING_BATCH_SIZE=1

#to generate BEARER_TOKEN:
#BEARER_TOKEN is a security token set for your Database Interface. It is the API key calling your own server. Create any key using https://jwt.io/. On Decoded tab “PayLoad” section:

#{
# “sub”: “1234567890”,
# “name”: “Write any name”,
# “iat”: 1516239022
#}
#Change the value to whatever you like. Then go back to Encoded tab and copy that generated token. Paste the key to the above export command. Your server will get this variable when it starts and set this as your security token. Save this token somewhere in a file because you need it later for sending the request.

