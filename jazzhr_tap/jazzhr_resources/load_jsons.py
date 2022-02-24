from os.path import join, dirname
import json

def load_jazzhr_key():
  keys_path = join(dirname(__file__), 'schemas/keys.json')
  with open(keys_path, encoding='utf-8') as json_keys:
    JAZZHR_KEY = json.load(json_keys)["jazzhr_key"]
  return JAZZHR_KEY

def load_schema(route):
  schema_path = join(dirname(__file__), f'schemas/{route}.json')
  with open(schema_path, encoding='utf-8') as json_schema:
    schema = json.load(json_schema)
  return schema