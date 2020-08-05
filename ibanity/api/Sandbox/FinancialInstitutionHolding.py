from collections import namedtuple
from ibanity import Ibanity
from ibanity.Flatten import flatten_json


def get_list(financial_institution_id, financial_institution_user_id, financial_institution_account_id, params={}):
    uri = Ibanity.client.api_schema["sandbox"]["financialInstitution"]["financialInstitutionAccount"]["financialInstitutionHoldings"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{financialInstitutionUserId}", financial_institution_user_id) \
        .replace("{financialInstitutionAccountId}", financial_institution_account_id)\
        .replace("{financialInstitutionHoldingId}", "")
    response = Ibanity.client.get(uri, params, None)
    return list(
        map(
            lambda holding:
            flatten_json(holding), response["data"]
        )
    )


def create(financial_institution_id, financial_institution_user_id, financial_institution_account_id, attributes):
    uri = Ibanity.client.api_schema["sandbox"]["financialInstitution"]["financialInstitutionAccount"]["financialInstitutionHoldings"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{financialInstitutionUserId}", financial_institution_user_id) \
        .replace("{financialInstitutionAccountId}", financial_institution_account_id)\
        .replace("{financialInstitutionHoldingId}", "")
    body = {
        "data": {
            "type": "financialInstitutionHolding",
            "attributes": attributes
        }
    }
    response = Ibanity.client.post(uri, body, {}, None)
    return flatten_json(response["data"])


def delete(financial_institution_id, financial_institution_user_id, financial_institution_account_id, id):
    uri = Ibanity.client.api_schema["sandbox"]["financialInstitution"]["financialInstitutionAccount"]["financialInstitutionHoldings"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{financialInstitutionUserId}", financial_institution_user_id) \
        .replace("{financialInstitutionAccountId}", financial_institution_account_id)\
        .replace("{financialInstitutionHoldingId}", id)
    response = Ibanity.client.delete(uri, {}, None)
    return flatten_json(response["data"])


def find(financial_institution_id, financial_institution_user_id, financial_institution_account_id, id):
    uri = Ibanity.client.api_schema["sandbox"]["financialInstitution"]["financialInstitutionAccount"]["financialInstitutionHoldings"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{financialInstitutionUserId}", financial_institution_user_id) \
        .replace("{financialInstitutionAccountId}", financial_institution_account_id)\
        .replace("{financialInstitutionHoldingId}", id)
    response = Ibanity.client.get(uri, {}, None)
    return flatten_json(response["data"])

