from collections import namedtuple
from ibanity import Ibanity
from ibanity.Flatten import flatten_json


def get_list(financial_institution_id, financial_institution_user_id, financial_institution_account_id, params={}):
    uri = Ibanity.client.api_schema["sandbox"]["financialInstitution"]["financialInstitutionAccount"]["financialInstitutionTransactions"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{financialInstitutionUserId}", financial_institution_user_id) \
        .replace("{financialInstitutionAccountId}", financial_institution_account_id)\
        .replace("{financialInstitutionTransactionId}", "")
    response = Ibanity.client.get(uri, params, None)
    return list(
        map(
            lambda transaction:
            flatten_json(transaction), response["data"]
        )
    )


def create(financial_institution_id, financial_institution_user_id, financial_institution_account_id, attributes):
    uri = Ibanity.client.api_schema["sandbox"]["financialInstitution"]["financialInstitutionAccount"]["financialInstitutionTransactions"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{financialInstitutionUserId}", financial_institution_user_id) \
        .replace("{financialInstitutionAccountId}", financial_institution_account_id)\
        .replace("{financialInstitutionTransactionId}", "")
    body = {
        "data": {
            "type": "financialInstitutionTransaction",
            "attributes": attributes
        }
    }
    response = Ibanity.client.post(uri, body, {}, None)
    return flatten_json(response["data"])


def delete(financial_institution_id, financial_institution_user_id, financial_institution_account_id, id):
    uri = Ibanity.client.api_schema["sandbox"]["financialInstitution"]["financialInstitutionAccount"]["financialInstitutionTransactions"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{financialInstitutionUserId}", financial_institution_user_id) \
        .replace("{financialInstitutionAccountId}", financial_institution_account_id)\
        .replace("{financialInstitutionTransactionId}", id)
    response = Ibanity.client.delete(uri, {}, None)
    return flatten_json(response["data"])


def find(financial_institution_id, financial_institution_user_id, financial_institution_account_id, id):
    uri = Ibanity.client.api_schema["sandbox"]["financialInstitution"]["financialInstitutionAccount"]["financialInstitutionTransactions"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{financialInstitutionUserId}", financial_institution_user_id) \
        .replace("{financialInstitutionAccountId}", financial_institution_account_id)\
        .replace("{financialInstitutionTransactionId}", id)
    response = Ibanity.client.get(uri, {}, None)
    return flatten_json(response["data"])

