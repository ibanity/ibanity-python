from collections import namedtuple


def create(client, financial_institution_id, attributes, customer_access_token):
    uri = client.api_schema["customer"]["financialInstitution"]["paymentInitiationRequests"]\
        .replace("{financialInstitutionId}", financial_institution_id)\
        .replace("{paymentInitiationRequestId}", "")

    body = {
        "data": {
            "type": "paymentInitiationRequest",
            "attributes": attributes
        }
    }
    response = client.post(uri, body, {}, customer_access_token)
    return __create_payment_initiation_request_named_tuple__(response["data"])


def find(client, financial_institution_id, id, customer_access_token):
    uri = client.api_schema["customer"]["financialInstitution"]["paymentInitiationRequests"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{paymentInitiationRequestId}", id)
    response = client.get(uri, {}, customer_access_token)
    return __create_payment_initiation_request_named_tuple__(response["data"])


def __create_payment_initiation_request_named_tuple__(payment_initiation_request):
    return namedtuple("PaymentInitiationRequest",
                      payment_initiation_request.keys())(**payment_initiation_request)
