import http.client
import ssl
import urllib
import json
import ibanity.Error


class Client:
    def __init__(self, certificate_path, key_path, key_passphrase, api_host):
        self.certificate_path = certificate_path
        self.key_path = key_path
        self.key_passphrase = key_passphrase
        self.api_host = api_host

    def get(self, uri, params, customer_access_token):
        return self.execute("GET", uri, {}, params=params, headers=self.__build_headers(customer_access_token))

    def post(self, uri, body, params, customer_access_token):
        return self.execute("POST", uri, body, params=params, headers=self.__build_headers(customer_access_token))

    def delete(self, uri, params, customer_access_token):
        return self.execute("DELETE", uri, {}, params=params, headers=self.__build_headers(customer_access_token))

    def put(self, uri, body, params, customer_access_token):
        return self.execute("PUT", uri, body, params=params, headers=self.__build_headers(customer_access_token))

    def execute(self, method, uri, body, params, headers):
        if params:
            uri = uri + "&" + urllib.urlencode(params)

        context = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(self.certificate_path, keyfile=self.key_path, password=self.key_passphrase)
        connection = http.client.HTTPSConnection(self.api_host, context=context)
        connection.request(method, uri, body=body, headers=headers)
        response = connection.getresponse()

        if response.code > 400:
            body = json.loads(response.read().decode('utf-8'))
            raise ibanity.Error(body["errors"])
        else:
            return json.loads(response.read().decode('utf-8'))

    def __build_headers(self, customer_access_token):
        authorization = ""
        if customer_access_token:
            authorization = "Bearer " + str(customer_access_token)

        return {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": authorization
        }
