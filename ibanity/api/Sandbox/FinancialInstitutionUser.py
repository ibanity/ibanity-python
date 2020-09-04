from collections import namedtuple
from ibanity import Ibanity
from ibanity.Flatten import flatten_json


def get_list(params={}):
    uri = Ibanity.client.api_schema["sandbox"]["financialInstitutionUsers"].replace("{financialInstitutionUserId}", "")
    response = Ibanity.client.get(uri, params, None)
    return list(
        map(
            lambda user:
            flatten_json(user), response["data"]
        )
    )

def create(attributes):
    uri = Ibanity.client.api_schema["sandbox"]["financialInstitutionUsers"].replace("{financialInstitutionUserId}", "")
    body = {
        "data": {
            "type": "financialInstitutionUser",
            "attributes": attributes
        }
    }
    response = Ibanity.client.post(uri, body, {}, None)
    return flatten_json(response["data"])


def delete(id):
    uri = Ibanity.client.api_schema["sandbox"]["financialInstitutionUsers"] \
        .replace("{financialInstitutionUserId}", id)
    response = Ibanity.client.delete(uri, {}, None)
    return flatten_json(response["data"])


def find(id):
    uri = Ibanity.client.api_schema["sandbox"]["financialInstitutionUsers"] \
        .replace("{financialInstitutionUserId}", id)
    response = Ibanity.client.get(uri, {}, None)
    return flatten_json(response["data"])

