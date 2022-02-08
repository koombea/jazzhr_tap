from jazzhr_tap import run_jazz_tap

route = "applicants2jobs"


def read_record(item):
  item["rating"] = int(item["rating"])
  return item


key_properties = ["id"]
run_jazz_tap(route, read_record, key_properties)
