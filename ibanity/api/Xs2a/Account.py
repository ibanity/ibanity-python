from collections import namedtuple
from ibanity import Ibanity
from ibanity.Flatten import flatten_json


def get_list(customer_access_token, params={}):
    uri = Ibanity.client.api_schema["customer"]["accounts"]
    response = Ibanity.client.get(uri, params, "Bearer " + str(customer_access_token))
    return list(
        map(
            lambda account:
            flatten_json(account), response["data"]
        )
    )


def get_list_for_financial_institution(financial_institution_id, customer_access_token, params={}):
    uri = Ibanity.client.api_schema["customer"]["financialInstitution"]["accounts"]\
        .replace("{financialInstitutionId}", financial_institution_id)\
        .replace("{accountId}", "")
    response = Ibanity.client.get(uri, params, "Bearer " + str(customer_access_token))
    return list(
        map(
            lambda account:
            flatten_json(account), response["data"]
        )
    )


def find(financial_institution_id, id, customer_access_token):
    uri = Ibanity.client.api_schema["customer"]["financialInstitution"]["accounts"]\
        .replace("{financialInstitutionId}", financial_institution_id)\
        .replace("{accountId}", id)
    response = Ibanity.client.get(uri, {}, "Bearer " + str(customer_access_token))
    return flatten_json(response["data"])
