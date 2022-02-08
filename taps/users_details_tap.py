from jazzhr_details_tap import run_jazz_tap

route = "users"
key_properties = ["id"]


def read_record(item):
  if not isinstance(item["user_activity"], list):
    item["user_activity"] = [item["user_activity"]]
  return item


run_jazz_tap(route, read_record, key_properties)