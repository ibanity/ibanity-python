from collections import namedtuple
from ibanity import Ibanity
from ibanity.Flatten import flatten_json_ponto as flatten_json


def get_list(access_token):
    uri = Ibanity.client.api_schema_ponto["accounts"] \
        .replace("{accountId}", "")
    response = Ibanity.client.get(uri, {}, access_token)
    return list(
        map(
            lambda account:
            flatten_json(account), response["data"]
        )
    )


def find(id, access_token):
    uri = Ibanity.client.api_schema_ponto["accounts"] \
        .replace("{accountId}", id)
    response = Ibanity.client.get(uri, {}, access_token)
    return flatten_json(response["data"])

