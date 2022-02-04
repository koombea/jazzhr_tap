from jazzhr_tap import run_jazz_tap
import json

json_schema = open('./schemas/users.json')
route = "users"
schema = json.load(json_schema)
key_properties = ["id"]
stream = "jazzhr_users"


def read_record(item):
  return item


run_jazz_tap(route, schema, stream, read_record, key_properties)
