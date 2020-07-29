from collections import namedtuple
from ibanity import Ibanity

def get_list(financial_institution_id, account_id, customer_access_token, params={}):
    uri = Ibanity.client.api_schema["customer"]["financialInstitution"]["holdings"]\
        .replace("{financialInstitutionId}", financial_institution_id)\
        .replace("{accountId}", account_id)\
        .replace("{holdingId}", "")
    response = Ibanity.client.get(uri, params, customer_access_token)
    return list(
        map(
            lambda holding:
            __create_holding_named_tuple__(holding), response["data"]
        )
    )


def find(financial_institution_id, account_id, id, customer_access_token):
    uri = Ibanity.client.api_schema["customer"]["financialInstitution"]["holdings"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{accountId}", account_id)\
        .replace("{holdingId}", id)
    response = Ibanity.client.get(uri, {}, customer_access_token)
    return __create_holding_named_tuple__(response["data"])


def __create_holding_named_tuple__(holding):
    return namedtuple("Holding", holding.keys())(**holding)
