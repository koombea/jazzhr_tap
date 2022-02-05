import json
import singer
import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv
with open('./schemas/files.json', encoding='utf-8') as json_schema:
  schema = json.load(json_schema)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
JAZZHR_KEY = os.environ.get("jazzhr_key")
current_applicant = None

endpoint = "https://api.resumatorapi.com/v1/"


def retrieve_applicants_per_page(page):
  authenticated_endpoint = f"{endpoint}applicants/page/{page}?apikey={JAZZHR_KEY}"
  api_response = requests.get(authenticated_endpoint).json()
  # next line is necessary because when only one element the response is not
  # a list but the only object
  if not isinstance(api_response, list):
    api_response = [api_response]
  return list(map(lambda d: d["id"], api_response))


def retrieve_files_per_page(page):
  global current_applicant
  authenticated_endpoint = f"{endpoint}files/applicant_id/{current_applicant}/page/{page}"
  file_data = {"apikey": JAZZHR_KEY}
  api_response = requests.get(authenticated_endpoint, json=file_data).json()
  # next line is necessary because when only one element the response is not
  # a list but the only object
  if not isinstance(api_response, list):
    api_response = [api_response]
  return api_response


def retrieve_all_items(retrieve_method):
  items = []
  pursue = True
  page = 1
  while pursue:
    response = retrieve_method(page)
    items = items + response
    page = page + 1
    if len(response) < 100:
      pursue = False
  return items


applicants = list(set(retrieve_all_items(retrieve_applicants_per_page)))
all_files = []

for a in applicants:
  current_applicant = a
  all_files = all_files + retrieve_all_items(retrieve_files_per_page)

stream = "jazzhr_files"

singer.write_schema(stream_name=stream, schema=schema, key_properties=["id"])

for file in all_files:
  file["file_size"] = int(file["file_size"])
  singer.write_record(stream_name=stream,
                      record=file)
