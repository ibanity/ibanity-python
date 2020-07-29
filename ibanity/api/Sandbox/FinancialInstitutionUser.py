from collections import namedtuple
from ibanity import Ibanity


def get_list(params={}):
    uri = Ibanity.client.api_schema["sandbox"]["financialInstitutionUsers"].replace("{financialInstitutionUserId}", "")
    response = Ibanity.client.get(uri, params, None)
    return list(
        map(
            lambda user:
            __create_user_named_tuple__(user), response["data"]
        )
    )

def create(attributes):
    uri = Ibanity.client.api_schema["sandbox"]["financialInstitutionUsers"].replace("{financialInstitutionUserId}", "")
    body = {
        "data": {
            "type": "financialInstitutionUser",
            "attributes": attributes
        }
    }
    response = Ibanity.client.post(uri, body, {}, None)
    return __create_user_named_tuple__(response["data"])


def delete(id):
    uri = Ibanity.client.api_schema["sandbox"]["financialInstitutionUsers"] \
        .replace("{financialInstitutionUserId}", id)
    response = Ibanity.client.delete(uri, {}, None)
    return __create_user_named_tuple__(response["data"])


def find(id):
    uri = Ibanity.client.api_schema["sandbox"]["financialInstitutionUsers"] \
        .replace("{financialInstitutionUserId}", id)
    response = Ibanity.client.get(uri, {}, None)
    return __create_user_named_tuple__(response["data"])


def __create_user_named_tuple__(user):
    return namedtuple("FinancialInstitutionUser", user.keys())(**user)
