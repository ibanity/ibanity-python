from collections import namedtuple
from ibanity import Ibanity
from ibanity.Flatten import flatten_json


def delete(customer_access_token):
    uri = Ibanity.client.api_schema["customer"]["self"]
    response = Ibanity.client.delete(uri, {}, None)
    return flatten_json(response["data"])
