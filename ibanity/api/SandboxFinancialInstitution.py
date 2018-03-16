from collections import namedtuple



def create(client, attributes):
    uri = client.api_schema["sandbox"]["financialInstitutions"].replace("{financialInstitutionId}", "")
    body = {
        "data": {
            "type": "financialInstitution",
            "attributes": attributes
        }
    }
    response = client.post(uri, body, {}, None)
    return __create_financial_institution_named_tuple__(response["data"])


def delete(client, id):
    uri = client.api_schema["sandbox"]["financialInstitutions"] \
        .replace("{financialInstitutionId}", id)
    response = client.delete(uri, {}, None)
    return __create_financial_institution_named_tuple__(response["data"])


def update(client, id, attributes):
    uri = client.api_schema["sandbox"]["financialInstitutions"] \
        .replace("{financialInstitutionId}", id)
    body = {
        "data": {
            "type": "financialInstitution",
            "attributes": attributes
        }
    }
    response = client.patch(uri, body, {}, None)
    return __create_financial_institution_named_tuple__(response["data"])


def __create_financial_institution_named_tuple__(financial_institution):
    return namedtuple("SandboxFinancialInstitution", financial_institution.keys())(**financial_institution)
