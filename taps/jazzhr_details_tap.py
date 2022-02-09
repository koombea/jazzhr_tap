import os
from os.path import join, dirname
import json
import singer
import requests
from dotenv import load_dotenv


def run_jazz_tap(route, read_record, key_properties):
  dotenv_path = join(dirname(__file__), '../.env')
  schema_path = join(dirname(__file__), f'../schemas/{route}_details.json')
  with open(schema_path, encoding='utf-8') as json_schema:
    schema = json.load(json_schema)
  load_dotenv(dotenv_path)
  stream = f"jazzhr_{route}_details"

  JAZZHR_KEY = os.environ.get("jazzhr_key")
  endpoint = "https://api.resumatorapi.com/v1/"
  page = 1

  def retrieve_jazzhr_items():
    authenticated_endpoint = f"{endpoint}{route}/page/{page}?apikey={JAZZHR_KEY}"
    api_response = requests.get(authenticated_endpoint).json()
    return [r["id"] for r in api_response]

  def retrieve_jazzhr_items_details(index):
    authenticated_endpoint = f"{endpoint}{route}/{index}?apikey={JAZZHR_KEY}"
    api_response = requests.get(authenticated_endpoint).json()
    return api_response

  singer.write_schema(
    stream_name=stream,
    schema=schema,
    key_properties=key_properties)
  items = []
  pursue = True
  while pursue:
    response = retrieve_jazzhr_items()
    items = items + response
    page = page + 1
    if len(response) < 100:
      pursue = False
  for item_ in items:

    item_details = retrieve_jazzhr_items_details(item_)
    singer.write_record(stream_name=stream,
                        record=read_record(item_details))
