from jazzhr_resources.jazzhr_tap import run_jazz_tap

route = "tasks"
key_properties = ["id"]


def read_record(item):
  item["due_whenever"] = (item["due_whenever"] == 'Yes')
  return item


def main():
  run_jazz_tap(route, read_record, key_properties)


if __name__ == "__main__":
  main()
