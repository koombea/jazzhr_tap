import json
from jazzhr_tap import run_jazz_tap
with open('./schemas/categories2applicants.json', encoding='utf-8') as json_schema:
  schema = json.load(json_schema)
route = "categories2applicants"
stream = "jazzhr_categories2applicants"
key_properties = ["id"]


def read_record(item):
  return item


run_jazz_tap(route, schema, stream, read_record, key_properties)
