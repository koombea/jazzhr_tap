from os.path import join, dirname
import json
from jazzhr_tap import run_jazz_tap

route = "applicants"
schema_path = join(dirname(__file__), '../schemas/applicants.json')
with open(schema_path, encoding='utf-8') as json_schema:
  schema = json.load(json_schema)
key_properties = ["id"]


def read_record(item):
  return item


run_jazz_tap(route, schema, read_record, key_properties)
