from collections import namedtuple
from ibanity import Ibanity
from ibanity.Flatten import flatten_json


def create(attributes, access_token):
    uri = Ibanity.client.api_schema_ponto["synchronizations"] \
	    .replace("{synchronizationId}", "")
    body = {
        "data": {
            "type": "synchronization",
            "attributes": attributes
            }
        }
    response = Ibanity.client.post(uri, body, {}, "Bearer " + str(access_token))
    return flatten_json(response["data"])


def find(id, access_token):
    uri = Ibanity.client.api_schema_ponto["synchronizations"] \
        .replace("{synchronizationId}", id)
    response = Ibanity.client.get(uri, {}, "Bearer " + str(access_token))
    return flatten_json(response["data"])

