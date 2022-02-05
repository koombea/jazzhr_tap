import json
from jazzhr_tap import run_jazz_tap

with open('./schemas/tasks.json', encoding='utf-8') as json_schema:
  schema = json.load(json_schema)
route = "tasks"
stream = "jazzhr_tasks"
key_properties = ["id"]


def read_record(item):
  item["due_whenever"] = True if item["due_whenever"] == 'Yes' else False
  return item


run_jazz_tap(route, schema, stream, read_record, key_properties)
