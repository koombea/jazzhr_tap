import os
from os.path import join, dirname
import json
import singer
import requests
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)


def run_jazz_tap(route, read_record, key_properties):
  schema_path = join(dirname(__file__), f'../schemas/{route}.json')
  with open(schema_path, encoding='utf-8') as json_schema:
    schema = json.load(json_schema)
    if route=="questionnaire_answers":
      for i in range(1, 21):
        key = '0' + str(i) if i < 10 else str(i)
        schema['properties']["answer_value_" + key] = {'type': ["string", "null"]}
        schema['properties']["answer_correct_" +
                            key] = {'type': ["string", "null"]}
  stream = "jazzhr_" + route
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
