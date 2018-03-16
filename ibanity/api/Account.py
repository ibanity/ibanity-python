from collections import namedtuple


def get_list(client, customer_access_token, params):
    uri = client.api_schema["customer"]["accounts"]
    response = client.get(uri, params, customer_access_token)
    return list(
        map(
            lambda account:
            __create_account_named_tuple__(account), response["data"]
        )
    )


def get_list_for_financial_institution(client, financial_institution_id, customer_access_token, params):
    uri = client.api_schema["customer"]["financialInstitution"]["accounts"]\
        .replace("{financialInstitutionId}", financial_institution_id)\
        .replace("{accountId}", "")
    response = client.get(uri, params, customer_access_token)
    return list(
        map(
            lambda account:
            __create_account_named_tuple__(account), response["data"]
        )
    )


def find(client, financial_institution_id, id, customer_access_token):
    uri = client.api_schema["customer"]["financialInstitution"]["accounts"]\
        .replace("{financialInstitutionId}", financial_institution_id)\
        .replace("{accountId}", id)
    response = client.get(uri, {}, customer_access_token)
    return __create_account_named_tuple__(response["data"])


def __create_account_named_tuple__(account):
    return namedtuple("Account", account.keys())(**account)
