import singer
from jazzhr_resources.http_request import call_api
from jazzhr_resources.load_jsons import load_schema


def run_jazz_tap(route, read_record, key_properties):
  schema = load_schema(route)
  if route == "questionnaire_answers":
    for i in range(1, 21):
      key = '0' + str(i) if i < 10 else str(i)
      schema['properties']["answer_value_" +
                             key] = {'type': ["string", "null"]}
      schema['properties']["answer_correct_" +
                             key] = {'type': ["string", "null"]}
  stream = "jazzhr_" + route
  endpoint = "https://api.resumatorapi.com/v1/"
  page = 1
  def retrieve_jazzhr():
    authenticated_endpoint = f"{endpoint}{route}/page/{page}"
    api_response =call_api(authenticated_endpoint)
    if not isinstance(api_response, list):
      api_response = [api_response]
    return api_response

  singer.write_schema(stream_name=stream, schema=schema,
                      key_properties=key_properties)

  items = []
  pursue = True
  while pursue:
    response = retrieve_jazzhr()
    items = items + response
    page = page + 1
    if len(response) < 100:
      pursue = False
  for item in items:
    singer.write_record(stream_name=stream,
                        record=read_record(item))
