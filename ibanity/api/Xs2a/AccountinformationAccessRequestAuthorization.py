from collections import namedtuple
from ibanity import Ibanity
from ibanity.Flatten import flatten_json


def create(financial_institution_id, account_information_access_request_id, customer_access_token, attributes):
    uri = Ibanity.client.api_schema["customer"]["financialInstitution"]["accountInformationAccessRequest"]["authorizations"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{accountInformationAccessRequestId}", account_information_access_request_id)
    body = {
        "data": {
            "type": "authorization",
            "attributes": attributes
        }
    }
    response = Ibanity.client.post(uri, body, {}, customer_access_token)
    return flatten_json(response["data"])
