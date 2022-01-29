from jazzhr_tap import run_jazz_tap

route = "contacts"
schema = {'properties': {
    'id': {'type': 'string'},
    'name_first': {'type': 'string'},
    'name_last': {'type': 'string'},
    'email': {'type': 'string'},
    'title': {'type': 'string'},
    'company_name': {'type': 'string'},
    'address': {'type': 'string'},
    'city': {'type': 'string'},
    'state': {'type': 'string'},
    'postal': {'type': 'string'},
    'phone_work': {'type': 'string'},
    'phone_mobile': {'type': 'string'},
    'phone_other': {'type': 'string'},
    'fax': {'type': 'string'},
    'twitter': {'type': 'string'},
    'notes': {'type': 'string'},
    'owner': {'type': 'string'},
    'date_created': { "type": "string", "format": "date"},
    'date_edited': { "type": "string", "format": "date"},
    'date_login': { "type": "string", "format": "date"}
    },
    "primary_key": "id"
  }
stream = "jazzhr_contacts"
def read_record(item):
  return item
run_jazz_tap(route, schema, stream, read_record)
