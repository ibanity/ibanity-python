from collections import namedtuple
from ibanity import Ibanity


def create(attributes, customer_access_token):
    uri = Ibanity.client.api_schema["customer"]["synchronizations"]\
        .replace("{synchronizationId}", "")

    body = {
        "data": {
            "type": "synchronization",
            "attributes": attributes
        }
    }
    response = Ibanity.client.post(uri, body, {}, customer_access_token)
    return __create_synchronization_named_tuple__(response["data"])


def find(id, customer_access_token):
    uri = Ibanity.client.api_schema["customer"]["synchronizations"] \
        .replace("{synchronizationId}", id)
    response = Ibanity.client.get(uri, {}, customer_access_token)
    return __create_synchronization_named_tuple__(response["data"])


def __create_synchronization_named_tuple__(synchronization):
    return namedtuple("Synchronization", synchronization.keys())(**synchronization)
