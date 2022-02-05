import json
from jazzhr_tap import run_jazz_tap

with open('./schemas/hires.json', encoding='utf-8') as json_schema:
  schema = json.load(json_schema)
route = "hires"
stream = "jazzhr_hires"
key_properties = ["id"]


def read_record(item):
  return item


run_jazz_tap(route, schema, stream, read_record, key_properties)
