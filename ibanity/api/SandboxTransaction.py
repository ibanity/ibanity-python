from collections import namedtuple


def get_list(client, financial_institution_id, sandbox_user_id, sandbox_account_id, params):
    uri = client.api_schema["sandbox"]["transactions"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{sandboxUserId}", sandbox_user_id) \
        .replace("{sandboxAccountId}", sandbox_account_id)\
        .replace("{sandboxTransactionId}", "")
    response = client.get(uri, params, None)
    return list(
        map(
            lambda transaction:
            __create_transaction_named_tuple__(transaction), response["data"]
        )
    )


def create(client, financial_institution_id, sandbox_user_id, sandbox_account_id, attributes):
    uri = client.api_schema["sandbox"]["transactions"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{sandboxUserId}", sandbox_user_id) \
        .replace("{sandboxAccountId}", sandbox_account_id)\
        .replace("{sandboxTransactionId}", "")
    body = {
        "data": {
            "type": "sandboxTransaction",
            "attributes": attributes
        }
    }
    response = client.post(uri, body, {}, None)
    return __create_transaction_named_tuple__(response["data"])


def delete(client, financial_institution_id, sandbox_user_id, sandbox_account_id, id):
    uri = client.api_schema["sandbox"]["transactions"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{sandboxUserId}", sandbox_user_id) \
        .replace("{sandboxAccountId}", sandbox_account_id)\
        .replace("{sandboxTransactionId}", id)
    response = client.delete(uri, {}, None)
    return __create_transaction_named_tuple__(response["data"])


def find(client, financial_institution_id, sandbox_user_id, sandbox_account_id, id):
    uri = client.api_schema["sandbox"]["transactions"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{sandboxUserId}", sandbox_user_id) \
        .replace("{sandboxAccountId}", sandbox_account_id)\
        .replace("{sandboxTransactionId}", id)
    response = client.get(uri, {}, None)
    return __create_transaction_named_tuple__(response["data"])


def __create_transaction_named_tuple__(transaction):
    return namedtuple("SandboxTransaction", transaction.keys())(**transaction)
