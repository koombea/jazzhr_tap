import json
from jazzhr_tap import run_jazz_tap
with open('./schemas/applicants2jobs.json', encoding='utf-8') as json_schema:
  schema = json.load(json_schema)
route = "applicants2jobs"
stream = "jazzhr_applicants2jobs"


def read_record(item):
  item["rating"] = int(item["rating"])
  return item


key_properties = ["id"]
run_jazz_tap(route, schema, stream, read_record, key_properties)
