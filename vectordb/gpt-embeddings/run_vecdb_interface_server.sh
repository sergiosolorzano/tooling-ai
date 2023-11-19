#!/bin/bash

echo ""
echo "Run Vector DB Interface Server for the Retrieval Plugin on Python3.10"
echo "When application is running, browser to http://localhost:8000/docs"
echo ""

# Prompt the user to confirm the environment variables have been added
echo "Confirm environment variables have been added. If yes, press enter to continue. Else cancel and add."
read confirmation

# Prompt the user to confirm the env has been activated
echo "Confirm Conda environment is active. Enter to continue else cancel"
read confirmation2

# Display messages for each command
echo "Changing directory..."
cd ~/my-repos/vectordb/gpt-embeddings/chatgpt-retrieval-plugin

echo "Installing poetry..."
pip install poetry

echo "Setting up virtual environment, run poetry shell and run the app on FastAPI..."
# Run the application using poetry run
poetry env use python3.10
echo ""
echo -e "\e[31mPlease enter 'exit' on CLI and press enter to switch to FastAPI Interface server.\e[0m"
echo ""
poetry shell
poetry install
poetry run start

