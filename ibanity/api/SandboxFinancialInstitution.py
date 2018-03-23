from collections import namedtuple
from ibanity import Ibanity



def create(attributes):
    uri = Ibanity.client.api_schema["sandbox"]["financialInstitutions"].replace("{financialInstitutionId}", "")
    body = {
        "data": {
            "type": "financialInstitution",
            "attributes": attributes
        }
    }
    response = Ibanity.client.post(uri, body, {}, None)
    return __create_financial_institution_named_tuple__(response["data"])


def delete(id):
    uri = Ibanity.client.api_schema["sandbox"]["financialInstitutions"] \
        .replace("{financialInstitutionId}", id)
    response = Ibanity.client.delete(uri, {}, None)
    return __create_financial_institution_named_tuple__(response["data"])


def update(id, attributes):
    uri = Ibanity.client.api_schema["sandbox"]["financialInstitutions"] \
        .replace("{financialInstitutionId}", id)
    body = {
        "data": {
            "type": "financialInstitution",
            "attributes": attributes
        }
    }
    response = Ibanity.client.patch(uri, body, {}, None)
    return __create_financial_institution_named_tuple__(response["data"])


def __create_financial_institution_named_tuple__(financial_institution):
    return namedtuple("SandboxFinancialInstitution", financial_institution.keys())(**financial_institution)
