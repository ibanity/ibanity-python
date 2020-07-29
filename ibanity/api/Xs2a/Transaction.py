from collections import namedtuple
from ibanity import Ibanity

def get_list(financial_institution_id, account_id, customer_access_token, params={}):
    uri = Ibanity.client.api_schema["customer"]["financialInstitution"]["transactions"]\
        .replace("{financialInstitutionId}", financial_institution_id)\
        .replace("{accountId}", account_id)\
        .replace("{transactionId}", "")
    response = Ibanity.client.get(uri, params, customer_access_token)
    return list(
        map(
            lambda transaction:
            __create_transaction_named_tuple__(transaction), response["data"]
        )
    )


def find(financial_institution_id, account_id, id, customer_access_token):
    uri = Ibanity.client.api_schema["customer"]["financialInstitution"]["transactions"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{accountId}", account_id)\
        .replace("{transactionId}", id)
    response = Ibanity.client.get(uri, {}, customer_access_token)
    return __create_transaction_named_tuple__(response["data"])


def __create_transaction_named_tuple__(transaction):
    return namedtuple("Transaction", transaction.keys())(**transaction)
