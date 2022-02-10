from jazzhr_resources.jazzhr_tap import run_jazz_tap

route = "categories"
key_properties = ["id"]


def read_record(item):
  return item


def main():
  run_jazz_tap(route, read_record, key_properties)
  
if __name__ == "__main__":
  main()
