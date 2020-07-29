from collections import namedtuple
from ibanity import Ibanity


def get_list(access_token):
    uri = Ibanity.client.api_schema_ponto["accounts"]
    response = Ibanity.client.get(uri, {}, access_token)
    return list(
        map(
            lambda account:
            __create_account_named_tuple__(account), response["data"]
        )
    )


def find(id, access_token):
    uri = Ibanity.client.api_schema_ponto["accounts"] \
        .replace("{accountId}", id)
    response = Ibanity.client.get(uri, {}, access_token)
    return __create_account_named_tuple__(response["data"])


def __create_account_named_tuple__(account):
    return namedtuple("Account", account.keys())(**account)
