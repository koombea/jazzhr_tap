from jazzhr_details_tap import run_jazz_tap

route = "jobs"
key_properties = ["id"]


def read_record(item):
  if not isinstance(item["job_applicants"], list):
    item["job_applicants"] = [item["job_applicants"]]
  item["minimum_salary"] = float(item["minimum_salary"])
  item["maximum_salary"] = float(item["maximum_salary"])
  return item


run_jazz_tap(route, read_record, key_properties)