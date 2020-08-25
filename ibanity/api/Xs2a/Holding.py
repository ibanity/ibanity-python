from collections import namedtuple
from ibanity import Ibanity
from ibanity.Flatten import flatten_json


def get_list(financial_institution_id, account_id, customer_access_token, params={}):
    uri = Ibanity.client.api_schema["customer"]["financialInstitution"]["holdings"]\
        .replace("{financialInstitutionId}", financial_institution_id)\
        .replace("{accountId}", account_id) \
        .replace("{holdingId}", "")
    response = Ibanity.client.get(uri, params, "Bearer " + str(customer_access_token))
    return list(
        map(
            lambda holding:
            flatten_json(holding), response["data"]
        )
    )


def find(financial_institution_id, account_id, id, customer_access_token):
    uri = Ibanity.client.api_schema["customer"]["financialInstitution"]["holdings"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{accountId}", account_id) \
        .replace("{holdingId}", id)
    response = Ibanity.client.get(uri, {}, "Bearer " + str(customer_access_token))
    return flatten_json(response["data"])
