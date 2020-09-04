from collections import namedtuple
from ibanity import Ibanity
from ibanity.Flatten import flatten_json


def create(application_customer_reference):
    uri = Ibanity.client.api_schema["customerAccessTokens"]
    body = {
        "data": {
            "type": "customerAccessToken",
            "attributes": {
                "applicationCustomerReference": str(application_customer_reference)
            }
        }
    }
    response = Ibanity.client.post(uri, body, {}, None)
    return flatten_json(response["data"])
