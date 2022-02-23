from os.path import join, dirname
import json
import singer
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import backoff
from requests.exceptions import HTTPError
from simplejson import JSONDecodeError


session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)


def run_jazz_tap(route, read_record, key_properties):
  keys_path = join(dirname(__file__), 'schemas/keys.json')
  with open(keys_path, encoding='utf-8') as json_keys:
    JAZZHR_KEY = json.load(json_keys)["jazzhr_key"]
  schema_path = join(dirname(__file__), f'schemas/{route}.json')
  with open(schema_path, encoding='utf-8') as json_schema:
    schema = json.load(json_schema)
    if route == "questionnaire_answers":
      for i in range(1, 21):
        key = '0' + str(i) if i < 10 else str(i)
        schema['properties']["answer_value_" +
                             key] = {'type': ["string", "null"]}
        schema['properties']["answer_correct_" +
                             key] = {'type': ["string", "null"]}
  stream = "jazzhr_" + route
  endpoint = "https://api.resumatorapi.com/v1/"
  page = 1
  @backoff.on_exception(backoff.constant,
                           (requests.exceptions.ConnectionError, HTTPError, JSONDecodeError),
                          max_tries=10,
                          interval=60)
  def retrieve_jazzhr():
    authenticated_endpoint = f"{endpoint}{route}/page/{page}?apikey={JAZZHR_KEY}"
    api_response = session.get(authenticated_endpoint).json()
    if not isinstance(api_response, list):
      api_response = [api_response]
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
