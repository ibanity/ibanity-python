from collections import namedtuple
from ibanity import Ibanity


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
    return __create_account_information_access_request_named_tuple__(response["data"])

def find(financial_institution_id, id, customer_access_token):
    uri = Ibanity.client.api_schema["customer"]["financialInstitution"]["accountInformationAccessRequests"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{accountInformationAccessRequestId}", id)
    response = Ibanity.client.get(uri, {}, customer_access_token)
    return __create_account_information_access_request_named_tuple__(response["data"])

def __create_account_information_access_request_named_tuple__(account_information_access_request):
    return namedtuple("AccountInformationAccessRequest",
                      account_information_access_request.keys())(**account_information_access_request)
