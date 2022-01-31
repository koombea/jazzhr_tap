from jazzhr_tap import run_jazz_tap

route = "activities"
schema = {'properties': {
    'id': {'type': 'string'},
    'category': {'type': 'string'},
    'team_id': {'type': 'string'},
    'user_id': {'type': 'string'},
    'object_id': {'type': 'string'},
    'action': {'type': 'string'},
    'date': { "type": "string", "format": "date"},
    'time': { "type": "string", "format": "time"}
    },
    "primary_key": "id"
  }
stream = "jazzhr_activities"
def read_record(item):
  return item
run_jazz_tap(route, schema, stream, read_record)