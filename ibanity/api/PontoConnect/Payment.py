from collections import namedtuple
from ibanity import Ibanity


def create(account_id, attributes, access_token):
    uri = Ibanity.client.api_schema_ponto["account"]["payments"] \
        .replace("{accountId}", account_id) \
	    .replace("{paymentId}", "")
    body = {
        "data": {
            "type": "payment",
            "attributes": attributes
            }
        }
    response = Ibanity.client.post(uri, body, {}, access_token)
    return __create_payment_named_tuple__(response["data"])


def find(account_id, id, access_token):
    uri = Ibanity.client.api_schema_ponto["account"]["payments"] \
        .replace("{accountId}", account_id) \
        .replace("{paymentId}", id)
    response = Ibanity.client.get(uri, {}, access_token)
    return __create_payment_named_tuple__(response["data"])


def delete(account_id, id, access_token):
    uri = Ibanity.client.api_schema_ponto["account"]["payments"] \
        .replace("{accountId}", account_id) \
        .replace("{paymentId}", id)
    response = Ibanity.client.delete(uri, {}, access_token)
    return __create_payment_named_tuple__(response["data"])

def __create_payment_named_tuple__(payment):
    return namedtuple("Payment", payment.keys())(**payment)
