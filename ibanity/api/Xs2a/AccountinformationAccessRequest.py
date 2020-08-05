from collections import namedtuple
from ibanity import Ibanity
from ibanity.Flatten import flatten_json


def create(financial_institution_id, customer_access_token, attributes):
    uri = Ibanity.client.api_schema["customer"]["financialInstitution"]["accountInformationAccessRequests"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{accountInformationAccessRequestId}", "")
    body = {
        "data": {
            "type": "accountinformationAccessRequest",
            "attributes": attributes
        }
    }
    response = Ibanity.client.post(uri, body, {}, customer_access_token)
    return flatten_json(response["data"])

def find(financial_institution_id, id, customer_access_token):
    uri = Ibanity.client.api_schema["customer"]["financialInstitution"]["accountInformationAccessRequests"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{accountInformationAccessRequestId}", id)
    response = Ibanity.client.get(uri, {}, customer_access_token)
    return flatten_json(response["data"])