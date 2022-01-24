from jazzhr_tap import run_jazz_tap

route = "jobs"
schema = {'properties': {
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
    'questionnaire': {'type': 'integer'}
    },
    "primary_key": "id"
  }
stream = "jazzhr_jobs"
def read_record(item):
  return {
      "id": item['id'], 
      'team_id': item["team_id"],
      'title': item["title"],
      'country_id': item["country_id"],
      'city': item["city"],
      'state': item["state"],
      'zip': item["zip"],
      'department': item["department"],
      'description': item["description"],
      'minimum_salary': float(item["minimum_salary"]),
      'maximum_salary': float(item["maximum_salary"]),
      'notes': item["notes"],
      'original_open_date': item["original_open_date"],
      'type': item["type"],
      'status': item["status"],
      'send_to_job_boards': item["send_to_job_boards"],
      'hiring_lead': item["hiring_lead"],
      'board_code': item["board_code"],
      'internal_code': item["internal_code"],
      'questionnaire': int(item["questionnaire"])
      }
run_jazz_tap(route, schema, stream, read_record)
