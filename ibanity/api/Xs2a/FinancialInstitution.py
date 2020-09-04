from collections import namedtuple
from ibanity import Ibanity
from ibanity.Flatten import flatten_json


def get_list(params={}):
    uri = Ibanity.client.api_schema["financialInstitutions"] \
        .replace("{financialInstitutionId}", "")
    response = Ibanity.client.get(uri, params, None)
    return list(
        map(
            lambda financial_institution:
            flatten_json(financial_institution), response["data"]
        )
    )

def create(attributes):
    uri = Ibanity.client.api_schema["sandbox"]["financialInstitutions"] \
        .replace("{financialInstitutionId}", "")
    body = {
        "data": {
            "type": "financialInstitution",
            "attributes": attributes
        }
    }
    response = Ibanity.client.post(uri, body, {}, None)
    return flatten_json(response["data"])


def delete(id):
    uri = Ibanity.client.api_schema["sandbox"]["financialInstitutions"] \
        .replace("{financialInstitutionId}", id)
    response = Ibanity.client.delete(uri, {}, None)
    return flatten_json(response["data"])


def update(id, attributes):
    uri = Ibanity.client.api_schema["sandbox"]["financialInstitutions"] \
        .replace("{financialInstitutionId}", id)
    body = {
        "data": {
            "type": "financialInstitution",
            "attributes": attributes
        }
    }
    response = Ibanity.client.patch(uri, body, {}, None)
    return flatten_json(response["data"])

def find(id):
    uri = Ibanity.client.api_schema["financialInstitutions"].replace("{financialInstitutionId}", id)
    response = Ibanity.client.get(uri, {}, None)
    return flatten_json(response["data"])
