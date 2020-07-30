from collections import namedtuple
from ibanity import Ibanity


def get_list(account_id, access_token):
    uri = Ibanity.client.api_schema_ponto["account"]["transactions"] \
	    .replace("{accountId}", account_id) \
		.replace("{transactionId}", "")
    response = Ibanity.client.get(uri, {}, access_token)
    return list(
        map(
            lambda transaction:
            __create_transaction_named_tuple__(transaction), response["data"]
        )
    )


def find(account_id, id, access_token):
    uri = Ibanity.client.api_schema_ponto["account"]["transactions"] \
        .replace("{accountId}", account_id) \
		.replace("{transactionId}", id)
    response = Ibanity.client.get(uri, {}, access_token)
    return __create_transaction_named_tuple__(response["data"])


def __create_transaction_named_tuple__(transaction):
    return namedtuple("transaction", transaction.keys())(**transaction)
