from collections import namedtuple
from ibanity import Ibanity
from ibanity.Flatten import flatten_json
from ibanity.Flatten import flatten_json


def create(financial_institution_id, attributes, customer_access_token):
    uri = Ibanity.client.api_schema["customer"]["financialInstitution"]["paymentInitiationRequests"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{paymentInitiationRequestId}", "")

    body = {
        "data": {
            "type": "paymentInitiationRequest",
            "attributes": attributes
        }
    }
    response = Ibanity.client.post(uri, body, {}, customer_access_token)
    return flatten_json(response["data"])


def find(financial_institution_id, id, customer_access_token):
    uri = Ibanity.client.api_schema["customer"]["financialInstitution"]["paymentInitiationRequests"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{paymentInitiationRequestId}", id)
    response = Ibanity.client.get(uri, {}, customer_access_token)
    return flatten_json(response["data"])

