from jazzhr_resources.jazzhr_details_tap import run_jazz_tap

route = "users"
key_properties = ["id"]


def read_record(item):
  if not isinstance(item["user_activity"], list):
    item["user_activity"] = [item["user_activity"]]
  return item


def main():
  run_jazz_tap(route, read_record, key_properties)


if __name__ == "__main__":
  main()
