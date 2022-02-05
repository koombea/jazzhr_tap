import json
from jazzhr_tap import run_jazz_tap
with open('./schemas/jobs.json', encoding='utf-8') as json_schema:
  schema = json.load(json_schema)
route = "jobs"
key_properties = ["id"]
stream = "jazzhr_jobs"


def read_record(item):
  item["minimum_salary"] = float(item["minimum_salary"])
  item["maximum_salary"] = float(item["maximum_salary"])
  return item


run_jazz_tap(route, schema, stream, read_record, key_properties)
