import ssl
import urllib.parse as urllib
from http.client import HTTPSConnection
from json import loads, dumps

import ibanity.Error


class Client:
    def __init__(self, certificate_path, key_path, key_passphrase, api_host, scheme="https", port="443"):
        self.scheme = scheme
        self.port = port
        self.certificate_path = certificate_path
        self.key_path = key_path
        self.key_passphrase = key_passphrase
        self.api_host = api_host
        self.base_uri = self.scheme + "://" + self.api_host
        self.schema = None

    @property
    def api_schema(self):
        if self.schema is None:
            self.schema = self.get(self.base_uri, {}, None)["links"]
        return self.schema

    def get(self, uri, params, customer_access_token):
        return self.execute("GET", uri, {}, params=params, headers=self.__build_headers(customer_access_token))

    def post(self, uri, body, params, customer_access_token):
        return self.execute("POST", uri, body, params=params, headers=self.__build_headers(customer_access_token))

    def delete(self, uri, params, customer_access_token):
        return self.execute("DELETE", uri, {}, params=params, headers=self.__build_headers(customer_access_token))

    def patch(self, uri, body, params, customer_access_token):
        return self.execute("PATCH", uri, body, params=params, headers=self.__build_headers(customer_access_token))

    def execute(self, method, uri, body, params, headers):
        if params:
            uri = uri + "&" + urllib.urlencode(params)

        context = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(self.certificate_path, keyfile=self.key_path, password=self.key_passphrase)
        connection = HTTPSConnection(self.api_host, context=context)
        connection.request(method, uri, body=dumps(body), headers=headers)
        response = connection.getresponse()

        if response.code > 400:
            body = loads(response.read().decode('utf-8'))
            raise ibanity.Error(body["errors"])
        else:
            return loads(response.read().decode('utf-8'))

    @staticmethod
    def __build_headers(customer_access_token):
        authorization = ""
        if customer_access_token:
            authorization = "Bearer " + str(customer_access_token)

        return {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": authorization
        }
