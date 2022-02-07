import os
from os.path import join, dirname
import singer
import requests
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)


def run_jazz_tap(route, schema, stream, read_record, key_properties):
  JAZZHR_KEY = os.environ.get("jazzhr_key")
  endpoint = "https://api.resumatorapi.com/v1/"
  page = 1

  def retrieve_jazzhr():
    authenticated_endpoint = f"{endpoint}{route}/page/{page}?apikey={JAZZHR_KEY}"
    api_response = requests.get(authenticated_endpoint).json()
    return api_response

  singer.write_schema(stream_name=stream, schema=schema,
                      key_properties=key_properties)

  items = []
  pursue = True
  while pursue:
    response = retrieve_jazzhr()
    items = items + response
    page = page + 1
    if len(response) < 100:
      pursue = False
  for item in items:
    singer.write_record(stream_name=stream,
                        record=read_record(item))
