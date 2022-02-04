from jazzhr_tap import run_jazz_tap
import json

json_schema = open('./schemas/activities.json')
route = "activities"
schema = json.load(json_schema)
stream = "jazzhr_activities"
key_properties = ["id"]


def read_record(item):
  return item


run_jazz_tap(route, schema, stream, read_record, key_properties)
