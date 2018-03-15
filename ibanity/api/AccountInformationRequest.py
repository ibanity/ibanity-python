from collections import namedtuple


def create(client, financial_institution_id, redirect_uri, consent_reference, customer_access_token):
    uri = client.api_schema["customer"]["financialInstitution"]["accountInformationAccessRequests"]\
        .replace("{financialInstitutionId}", financial_institution_id)
    body = {
        "data": {
            "type": "accountinformationAccessRequest",
            "attributes": {
                "redirectUri": redirect_uri,
                "consentReference": consent_reference
            }
        }
    }
    response = client.post(uri, body, {}, customer_access_token)
    return __create_account_information_access_request_named_tuple__(response["data"])

def __create_account_information_access_request_named_tuple__(account_information_access_request):
    return namedtuple("AccountInformationAccessRequest",
                      account_information_access_request.keys())(**account_information_access_request)
