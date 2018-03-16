from collections import namedtuple


def get_list_for_financial_institution(client, financial_institution_id, sandbox_user_id, params):
    uri = client.api_schema["sandbox"]["accounts"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{sandboxUserId}", sandbox_user_id) \
        .replace("{sandboxAccountId}", "")
    print(uri)
    response = client.get(uri, params, None)
    return list(
        map(
            lambda account:
            __create_account_named_tuple__(account), response["data"]
        )
    )


def create(client, financial_institution_id, sandbox_user_id, attributes):
    uri = client.api_schema["sandbox"]["accounts"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{sandboxUserId}", sandbox_user_id) \
        .replace("{sandboxAccountId}", "")
    body = {
        "data": {
            "type": "sandboxAccount",
            "attributes": attributes
        }
    }
    response = client.post(uri, body, {}, None)
    return __create_account_named_tuple__(response["data"])


def delete(client, financial_institution_id, sandbox_user_id, id):
    uri = client.api_schema["sandbox"]["accounts"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{sandboxUserId}", sandbox_user_id) \
        .replace("{sandboxAccountId}", id)
    response = client.delete(uri, {}, None)
    return __create_account_named_tuple__(response["data"])


def find(client, financial_institution_id, sandbox_user_id, id):
    uri = client.api_schema["sandbox"]["accounts"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{sandboxUserId}", sandbox_user_id) \
        .replace("{sandboxAccountId}", id)
    response = client.get(uri, {}, None)
    return __create_account_named_tuple__(response["data"])


def __create_account_named_tuple__(account):
    return namedtuple("SandboxAccount", account.keys())(**account)
