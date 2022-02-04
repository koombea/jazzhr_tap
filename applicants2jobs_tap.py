from jazzhr_tap import run_jazz_tap
import json

json_schema = open('./schemas/applicants2jobs.json')
route = "applicants2jobs"
schema = json.load(json_schema)
stream = "jazzhr_applicants2jobs"


def read_record(item):
  item["rating"] = int(item["rating"])
  return item


key_properties = ["id"]
run_jazz_tap(route, schema, stream, read_record, key_properties)
