from collections import namedtuple
from ibanity import Ibanity
from ibanity.Flatten import flatten_json


def get_list(access_token = None):
    uri = Ibanity.client.api_schema_ponto["financialInstitutions"] \
    .replace("{financialInstitutionId}", "")
    if (response == None):
        response = Ibanity.client.get(uri, {}, None)
    else:
        response = Ibanity.client.get(uri, {}, "Bearer " + str(access_token))
    return list(
        map(
            lambda financial_institution:
            flatten_json(financial_institution), response["data"]
        )
    )


def find(id):
    uri = Ibanity.client.api_schema_ponto["financialInstitutions"] \
        .replace("{financialInstitutionId}", id)
    response = Ibanity.client.get(uri, {}, None)
    return flatten_json(response["data"])

