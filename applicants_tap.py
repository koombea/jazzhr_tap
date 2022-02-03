from jazzhr_tap import run_jazz_tap

route = "applicants"
schema = {"type": "object",
  'properties': {
    'id': {'type': 'string'},
    'first_name': {'type': 'string'},
    'last_name': {'type': 'string'},
    'prospect_phone': {'type': 'string'},
    'apply_date': { "type": "string", "format": "date"},
    'job_id': {'type': 'string'},
    'job_title': {'type': 'string'}
    }
  }
stream = "jazzhr_applicants"
key_properties=["id"]
def read_record(item):
  return item
run_jazz_tap(route, schema, stream, read_record, key_properties)