from collections import namedtuple
from ibanity import Ibanity
from ibanity.Flatten import flatten_json


def get_list(account_id, access_token):
    uri = Ibanity.client.api_schema_ponto["account"]["transactions"] \
	    .replace("{accountId}", account_id) \
		.replace("{transactionId}", "")
    response = Ibanity.client.get(uri, {}, access_token)
    return list(
        map(
            lambda transaction:
            flatten_json(transaction), response["data"]
        )
    )


def find(account_id, id, access_token):
    uri = Ibanity.client.api_schema_ponto["account"]["transactions"] \
        .replace("{accountId}", account_id) \
		.replace("{transactionId}", id)
    response = Ibanity.client.get(uri, {}, access_token)
    return flatten_json(response["data"])

