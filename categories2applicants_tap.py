from jazzhr_tap import run_jazz_tap

route = "categories2applicants"
schema = {"type": "object",
  'properties': {
    'id': {'type': 'string'},
    'applicant_id': {'type': 'string'},
    'category_id': {'type': 'string'}
    }
  }
stream = "jazzhr_categories2applicants"
key_properties=["id"]
def read_record(item):
  return item
run_jazz_tap(route, schema, stream, read_record, key_properties)