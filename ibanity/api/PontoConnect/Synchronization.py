from collections import namedtuple
from ibanity import Ibanity


def create(attributes, access_token):
    uri = Ibanity.client.api_schema_ponto["synchronizations"] \
	    .replace("{synchronizationId}", "")
    body = {
        "data": {
            "type": "synchronization",
            "attributes": attributes
            }
        }
    }
    response = Ibanity.client.post(uri, body, {}, access_token)
    return __create_synchronization_named_tuple__(response["data"])


def find(id, access_token):
    uri = Ibanity.client.api_schema_ponto["synchronizations"] \
        .replace("{synchronizationId}", id)
    response = Ibanity.client.get(uri, {}, access_token)
    return __create_synchronization_named_tuple__(response["data"])


def __create_synchronization_named_tuple__(synchronization):
    return namedtuple("Synchronization", synchronization.keys())(**synchronization)
