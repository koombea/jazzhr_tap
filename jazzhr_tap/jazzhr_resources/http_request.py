import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import backoff
from requests.exceptions import HTTPError
from simplejson import JSONDecodeError
from jazzhr_resources.load_jsons import load_jazzhr_key


session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)
JAZZHR_KEY=load_jazzhr_key()

@backoff.on_exception(backoff.constant,
                           (requests.exceptions.ConnectionError, HTTPError, JSONDecodeError),
                          max_tries=10,
                          interval=60)
def call_api(url):
  api_response = session.get(f"{url}?apikey={JAZZHR_KEY}").json()
  return api_response