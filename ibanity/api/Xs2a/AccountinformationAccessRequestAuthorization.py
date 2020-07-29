from collections import namedtuple
from ibanity import Ibanity


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
    return __create_account_information_access_request_authorization_named_tuple__(response["data"])

def __create_account_information_access_request_authorization_named_tuple__(account_information_access_request_authorization):
    return namedtuple("AccountInformationAccessRequest",
                      account_information_access_request_authorization.keys())(**account_information_access_request_authorization)
