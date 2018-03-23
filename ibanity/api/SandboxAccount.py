from collections import namedtuple
from ibanity import Ibanity


def get_list_for_financial_institution(financial_institution_id, sandbox_user_id, params={}):
    uri = Ibanity.client.api_schema["sandbox"]["accounts"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{sandboxUserId}", sandbox_user_id) \
        .replace("{sandboxAccountId}", "")
    response = Ibanity.client.get(uri, params, None)
    return list(
        map(
            lambda account:
            __create_account_named_tuple__(account), response["data"]
        )
    )


def create(financial_institution_id, sandbox_user_id, attributes):
    uri = Ibanity.client.api_schema["sandbox"]["accounts"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{sandboxUserId}", sandbox_user_id) \
        .replace("{sandboxAccountId}", "")
    body = {
        "data": {
            "type": "sandboxAccount",
            "attributes": attributes
        }
    }
    response = Ibanity.client.post(uri, body, {}, None)
    return __create_account_named_tuple__(response["data"])


def delete(financial_institution_id, sandbox_user_id, id):
    uri = Ibanity.client.api_schema["sandbox"]["accounts"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{sandboxUserId}", sandbox_user_id) \
        .replace("{sandboxAccountId}", id)
    response = Ibanity.client.delete(uri, {}, None)
    return __create_account_named_tuple__(response["data"])


def find(financial_institution_id, sandbox_user_id, id):
    uri = Ibanity.client.api_schema["sandbox"]["accounts"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{sandboxUserId}", sandbox_user_id) \
        .replace("{sandboxAccountId}", id)
    response = Ibanity.client.get(uri, {}, None)
    return __create_account_named_tuple__(response["data"])


def __create_account_named_tuple__(account):
    return namedtuple("SandboxAccount", account.keys())(**account)
