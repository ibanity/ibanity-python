from collections import namedtuple
from ibanity import Ibanity
from ibanity.Flatten import flatten_json


def create(financial_institution_id, payment_initiation_request_id, attributes, customer_access_token):
    uri = Ibanity.client.api_schema["customer"]["financialInstitution"]["paymentInitiationRequest"]["authorizations"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{paymentInitiationRequestId}", payment_initiation_request_id)

    body = {
        "data": {
            "type": "authorization",
            "attributes": attributes
        }
    }
    response = Ibanity.client.post(uri, body, {}, "Bearer " + str(customer_access_token))
    return flatten_json(response["data"])

