from jazzhr_tap import run_jazz_tap

route = "categories2applicants"
key_properties = ["id"]


def read_record(item):
  return item


run_jazz_tap(route, read_record, key_properties)
