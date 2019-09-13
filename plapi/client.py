import requests
from requests.auth import HTTPBasicAuth


__author__ = "Petro-Logistics <info@petro-logistics.com>"
__version__ = "0.1.0"


class PLAPIClientError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return repr(self.msg)


class PLAPIClient:
    def __init__(self, api_url, api_key, api_hash, http_user, http_pass):
        """ __init__()
            Instantiates an instance of PLAPIClient. Takes parameters for authentication and such (see below).
            Parameters:
                api_endpoint: Which API to use (eg. https://secure.petro-logistics.com/api/v2/movementsdata).
                api_key: Your API key.
                api_hash: Your API hash.
                http_user: Your HTTP user.
                http_pass: Your HTTP password.
        """
        self.base_url = api_url
        self.api_key = api_key
        self.api_hash = api_hash
        self.http_user = http_user
        self.http_pass = http_pass


    def execute(self, query_name):
        """ execute(self)
            Executes the API query.
            Parameters:
                query_name: eg. Angola_Test_Data
        """
        payload = {'api_key': self.api_key, 'api_hash': self.api_hash, 'format': 'json', 'query_name': query_name, 'csv_with_headers': '1'}
        r = requests.post(self.base_url, data=payload, auth=HTTPBasicAuth(self.http_user, self.http_pass))

        return r.json()
