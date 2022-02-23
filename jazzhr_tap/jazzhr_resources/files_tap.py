import json
from os.path import join, dirname
import singer
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry


session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)


def main():
  keys_path = join(dirname(__file__), 'schemas/keys.json')
  with open(keys_path, encoding='utf-8') as json_keys:
    JAZZHR_KEY = json.load(json_keys)["jazzhr_key"]
  schema_path = join(dirname(__file__), 'schemas/files.json')
  with open(schema_path, encoding='utf-8') as json_schema:
    schema = json.load(json_schema)
  current_applicant = None

  endpoint = "https://api.resumatorapi.com/v1/"

  def retrieve_applicants_per_page(page):
    authenticated_endpoint = f"{endpoint}applicants/page/{page}?apikey={JAZZHR_KEY}"
    api_response = session.get(authenticated_endpoint).json()
    if not isinstance(api_response, list):
      api_response = [api_response]
    return [r["id"] for r in api_response]

  def retrieve_files_per_page(page):
    authenticated_endpoint = f"{endpoint}files/applicant_id/{current_applicant}/page/{page}"
    file_data = {"apikey": JAZZHR_KEY}
    api_response = session.get(authenticated_endpoint, json=file_data).json()
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


if __name__ == "__main__":
  main()
