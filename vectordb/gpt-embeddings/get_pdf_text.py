#!/usr/bin/env python3

from pathlib import Path
import os
import argparse
import sys
from PyPDF2 import PdfReader 
import requests
import subprocess

pdf_source_file_url="https://www.bankofengland.co.uk/-/media/boe/files/monetary-policy-report/2023/november/monetary-policy-report-november-2023.pdf"
pdf_sections = [(5,33),(35,78),(79,102)]
full_text_pdf_list = []
destination_files_dir="destFilesDir"
source_files_dir="databankDir"
dest_fname="extracted_pages"

#cli help
parser = argparse.ArgumentParser(
                    prog='LLM enhanced with embeddings',
                    description='Enhance gpt knowledge with embeddings')

parser.add_argument('-s', '--source', metavar='databankDir', type=str, help='Directory path to download the source file')
parser.add_argument('-d', '--destination', metavar='destFilesDir', type=str, help='Directory path to save chunked pages of the source file')

args = parser.parse_args()
print()

#export variables
# env_file_path = Path(os.environ['PWD'],"env_vars.sh")
# # Use subprocess to execute the shell script and capture its output
# result = subprocess.run(f"bash -c 'source {env_file_path} && env'", shell=True, stdout=subprocess.PIPE)

# # Decode the output and split environment variables
# output = result.stdout.decode('utf-8')
# env_vars = [line.split('=', 1) for line in output.splitlines()]

# # Update Python's environment with the retrieved variables
# for key, value in env_vars:
#     if key:
#         key = key.strip()
#         value = value.strip().strip('"') if value else ''
#         if value:
#             # Set the environment variables within Python
#             subprocess.run(f'export {key}={value}', shell=True)

#create dirs
if not os.path.exists(destination_files_dir):
	os.makedirs(destination_files_dir)
if not os.path.exists(source_files_dir):
	os.makedirs(source_files_dir)

#get pdf
print(); print("-" * 40); print()
print("\033[43mGet Source Document:\033[0m")
resp = requests.get(pdf_source_file_url)
if resp.status_code==200:
	print(f"\033[92;1mGet Success\033[0m")
	source_fname=os.path.basename(pdf_source_file_url)
else:
	print(f"\033[91m[ERROR] Get Failed.\033[0m")

#save pdf to source dir
#dest_path = os.path.join(os.environ['PWD'],destination_files_dir,dest_fname)
dest_path=Path(os.environ['PWD'],source_files_dir,source_fname)
with open(dest_path,"wb") as f:
	f.write(resp.content)
	print(f"Source doc saved to {dest_path}")

# creating a pdf reader object 
reader = PdfReader(dest_path)
  
# printing number of pages in pdf file
print(); print("-" * 40); print()
print("\033[43mChunk Source Document Pages:\033[0m")
pages = reader.pages
print("Pages in source file:",len(pages)) 
  
# getting a specific page from the pdf file
for count, page in enumerate(pages):
	page_text = reader.pages[count]
	# extracting text from page 
	text = str(page.extract_text())
	
	# Try to decode the text as UTF-8.
	if not isinstance(text,bytes):
		text = text.encode("utf-8")
		#print("ENCODING TO UTF")
	try:
		text = text.decode('utf-8')
	except UnicodeDecodeError:
		# If the text cannot be decoded as UTF-8, try to decode it as Latin-1.
		# Latin-1 is a superset of ASCII, so this will ensure that all characters
		# are decoded correctly.
		text = text.decode('latin-1')
		#print("DECODE FAIL")

	#full_text_pdf_list.append("page "+ str(count) + ":" +text)
	#full_text_pdf_list.append(text)

#print(full_text_pdf_list)

	filename = "".join([dest_fname, "_", str(count), ".txt"])
	with open(Path(os.environ['PWD'], destination_files_dir, filename), "w", encoding='utf-8') as filedata:
		#for item in full_text_pdf_list:
		filedata.write("%s\n" % text)
		print(f"Saved page {count} to file",filename)

	filedata.close()
#filedata = open(Path(os.environ['PWD'], destination_files_dir, dest_fname))
#print(filedata.read())