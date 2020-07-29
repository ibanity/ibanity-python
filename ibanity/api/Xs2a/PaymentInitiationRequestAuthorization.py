from collections import namedtuple
from ibanity import Ibanity


def create(financial_institution_id, payment_initiation_request_id, attributes, customer_access_token):
    uri = Ibanity.client.api_schema["customer"]["financialInstitution"]["paymentInitiationRequest"]["authorizations"]\
        .replace("{financialInstitutionId}", financial_institution_id)\
        .replace("{paymentInitiationRequestId}", payment_initiation_request_id)

    body = {
        "data": {
            "type": "authorization",
            "attributes": attributes
        }
    }
    response = Ibanity.client.post(uri, body, {}, customer_access_token)
    return __create_payment_initiation_request_authorization_named_tuple__(response["data"])


def __create_payment_initiation_request_authorization_named_tuple__(payment_initiation_request_authorization):
    return namedtuple("PaymentInitiationRequest",
                      payment_initiation_request_authorization.keys())(**payment_initiation_request_authorization)
