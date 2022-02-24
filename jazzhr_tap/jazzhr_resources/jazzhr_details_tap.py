import singer
from jazzhr_resources.http_request import call_api
from jazzhr_resources.load_jsons import load_schema


def run_jazz_tap(route, read_record, key_properties):
  schema = load_schema(route+"_details")
  stream = f"jazzhr_{route}_details"
  endpoint = "https://api.resumatorapi.com/v1/"
  page = 1

  def retrieve_jazzhr_items():
    authenticated_endpoint = f"{endpoint}{route}/page/{page}"
    api_response = call_api(authenticated_endpoint)
    if not isinstance(api_response, list):
      api_response = [api_response]
    return [r["id"] for r in api_response]

  def retrieve_jazzhr_items_details(index):
    authenticated_endpoint = f"{endpoint}{route}/{index}"
    api_response = call_api(authenticated_endpoint)
    return api_response

  singer.write_schema(
    stream_name=stream,
    schema=schema,
    key_properties=key_properties)
  items = []
  pursue = True
  while pursue:
    response = retrieve_jazzhr_items()
    items = items + response
    page = page + 1
    if len(response) < 100:
      pursue = False
  for item_ in items:

    item_details = retrieve_jazzhr_items_details(item_)
    singer.write_record(stream_name=stream,
                        record=read_record(item_details))
