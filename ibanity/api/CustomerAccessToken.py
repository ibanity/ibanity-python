from collections import namedtuple


def create(client, application_customer_reference):
    uri = client.api_schema["customerAccessTokens"]
    body = {
        "data": {
            "type": "customerAccessToken",
            "attributes": {
                "applicationCustomerReference": str(application_customer_reference)
            }
        }
    }
    response = client.post(uri, body, {}, None)
    return __create_customer_access_token_named_tuple__(response["data"])


def __create_customer_access_token_named_tuple__(customer_access_token):
    return namedtuple("CustomerAccessToken", customer_access_token.keys())(**customer_access_token)
