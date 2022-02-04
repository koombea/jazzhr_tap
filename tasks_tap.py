from jazzhr_tap import run_jazz_tap
import json

json_schema = open('./schemas/tasks.json')
route = "tasks"
schema = json.load(json_schema)
stream = "jazzhr_tasks"
key_properties = ["id"]


def read_record(item):
  item["due_whenever"] = True if item["due_whenever"] == 'Yes' else False
  return item


run_jazz_tap(route, schema, stream, read_record, key_properties)
