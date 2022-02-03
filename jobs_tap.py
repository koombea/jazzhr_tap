from jazzhr_tap import run_jazz_tap

route = "jobs"
schema = {"type": "object",
  'properties': {
    'id': {'type': 'string'},
    'team_id': {'type': 'string'},
    'title': {'type': 'string'},
    'country_id': {'type': 'string'},
    'city': {'type': 'string'},
    'state': {'type': 'string'},
    'zip': {'type': 'string'},
    'department': {'type': 'string'},
    'description': {'type': 'string'},
    'minimum_salary': {'type': 'number'},
    'maximum_salary': {'type': 'number'},
    'notes': {'type': 'string'},
    'original_open_date': { "type": "string", "format": "date"},
    'type': {'type': 'string'},
    'status': {'type': 'string'},
    'send_to_job_boards': {'type': 'string'},
    'hiring_lead': {'type': 'string'},
    'board_code': {'type': 'string'},
    'internal_code': {'type': 'string'},
    'questionnaire': {'type': 'string'}
    }
  }
key_properties=["id"]
stream = "jazzhr_jobs"
def read_record(item):
  item["minimum_salary"] = float(item["minimum_salary"])
  item["maximum_salary"] = float(item["maximum_salary"])
  return item
run_jazz_tap(route, schema, stream, read_record, key_properties)
