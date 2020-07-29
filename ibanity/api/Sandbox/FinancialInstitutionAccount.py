from collections import namedtuple
from ibanity import Ibanity


def get_list_for_financial_institution(financial_institution_id, financial_institution_user_id, params={}):
    uri = Ibanity.client.api_schema["sandbox"]["financialInstitution"]["financialInstitutionAccounts"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{financialInstitutionUserId}", financial_institution_user_id) \
        .replace("{financialInstitutionAccountId}", "")
    response = Ibanity.client.get(uri, params, None)
    return list(
        map(
            lambda account:
            __create_account_named_tuple__(account), response["data"]
        )
    )


def create(financial_institution_id, financial_institution_user_id, attributes):
    uri = Ibanity.client.api_schema["sandbox"]["financialInstitution"]["financialInstitutionAccounts"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{financialInstitutionUserId}", financial_institution_user_id) \
        .replace("{financialInstitutionAccountId}", "")
    body = {
        "data": {
            "type": "financialInstitutionAccount",
            "attributes": attributes
        }
    }
    response = Ibanity.client.post(uri, body, {}, None)
    return __create_account_named_tuple__(response["data"])


def delete(financial_institution_id, financial_institution_user_id, id):
    uri = Ibanity.client.api_schema["sandbox"]["financialInstitution"]["financialInstitutionAccounts"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{financialInstitutionUserId}", financial_institution_user_id) \
        .replace("{financialInstitutionAccountId}", id)
    response = Ibanity.client.delete(uri, {}, None)
    return __create_account_named_tuple__(response["data"])


def find(financial_institution_id, financial_institution_user_id, id):
    uri = Ibanity.client.api_schema["sandbox"]["financialInstitution"]["financialInstitutionAccounts"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{financialInstitutionUserId}", financial_institution_user_id) \
        .replace("{financialInstitutionAccountId}", id)
    response = Ibanity.client.get(uri, {}, None)
    return __create_account_named_tuple__(response["data"])


def __create_account_named_tuple__(account):
    return namedtuple("FinancialInstitutionAccount", account.keys())(**account)
