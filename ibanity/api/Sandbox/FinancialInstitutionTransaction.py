from collections import namedtuple
from ibanity import Ibanity


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
            __create_transaction_named_tuple__(transaction), response["data"]
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
    return __create_transaction_named_tuple__(response["data"])


def delete(financial_institution_id, financial_institution_user_id, financial_institution_account_id, id):
    uri = Ibanity.client.api_schema["sandbox"]["financialInstitution"]["financialInstitutionAccount"]["financialInstitutionTransactions"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{financialInstitutionUserId}", financial_institution_user_id) \
        .replace("{financialInstitutionAccountId}", financial_institution_account_id)\
        .replace("{financialInstitutionTransactionId}", id)
    response = Ibanity.client.delete(uri, {}, None)
    return __create_transaction_named_tuple__(response["data"])


def find(financial_institution_id, financial_institution_user_id, financial_institution_account_id, id):
    uri = Ibanity.client.api_schema["sandbox"]["financialInstitution"]["financialInstitutionAccount"]["financialInstitutionTransactions"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{financialInstitutionUserId}", financial_institution_user_id) \
        .replace("{financialInstitutionAccountId}", financial_institution_account_id)\
        .replace("{financialInstitutionTransactionId}", id)
    response = Ibanity.client.get(uri, {}, None)
    return __create_transaction_named_tuple__(response["data"])


def __create_transaction_named_tuple__(transaction):
    return namedtuple("FinancialInstitutionTransaction", transaction.keys())(**transaction)
