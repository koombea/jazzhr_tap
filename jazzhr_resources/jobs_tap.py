from jazzhr_resources.jazzhr_tap import run_jazz_tap

route = "jobs"
key_properties = ["id"]


def read_record(item):
  item["minimum_salary"] = float(item["minimum_salary"])
  item["maximum_salary"] = float(item["maximum_salary"])
  return item


def main():
  run_jazz_tap(route, read_record, key_properties)


if __name__ == "__main__":
  main()
