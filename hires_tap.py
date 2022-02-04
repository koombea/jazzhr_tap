from jazzhr_tap import run_jazz_tap
import json

json_schema = open('./schemas/hires.json')
route = "hires"
schema = json.load(json_schema)
stream = "jazzhr_hires"
key_properties = ["id"]


def read_record(item):
  return item


run_jazz_tap(route, schema, stream, read_record, key_properties)
