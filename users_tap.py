from jazzhr_tap import run_jazz_tap

route = "users"
schema = {'properties': {
    'id': {'type': 'string'},
    'type': {'type': 'string'},
    'last_name': {'type': 'string'},
    'first_name': {'type': 'string'},
    'date_created': { "type": "string", "format": "date"},
    'email': {'type': 'string'}
    },
    "primary_key": "id"
  }
stream = "jazzhr_users"
def read_record(item):
  return {
    "id": item['id'], 
    'type': item["type"],
    'last_name': item["last_name"],
    'first_name': item["first_name"],
    'date_created': item["date_created"],
    'email': item["email"]
    }
run_jazz_tap(route, schema, stream, read_record)