from jazzhr_tap import run_jazz_tap
import json

json_schema = open('./schemas/categories2applicants.json')
route = "categories2applicants"
schema = json.load(json_schema)
stream = "jazzhr_categories2applicants"
key_properties = ["id"]


def read_record(item):
  return item


run_jazz_tap(route, schema, stream, read_record, key_properties)
