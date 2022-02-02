from jazzhr_tap import run_jazz_tap

route = "categories"
schema = {'properties': {
    'id': {'type': 'string'},
    'name': {'type': 'string'},
    'status': {'type': 'string'},
    'created_by': {'type': 'string'},
    'date_created': { "type": "string", "format": "date"}
    }
  }
stream = "jazzhr_categories"
key_properties=["id"]
def read_record(item):
  return item
run_jazz_tap(route, schema, stream, read_record, key_properties)