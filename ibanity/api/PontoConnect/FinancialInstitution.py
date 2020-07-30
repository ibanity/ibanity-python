from collections import namedtuple
from ibanity import Ibanity


def get_list(access_token = None):
    uri = Ibanity.client.api_schema_ponto["financialInstitutions"] \
    .replace("{financialInstitutionId}", "")
    response = Ibanity.client.get(uri, {}, access_token)
    return list(
        map(
            lambda financial_institution:
            __create_financial_institution_named_tuple__(financial_institution), response["data"]
        )
    )


def find(id):
    uri = Ibanity.client.api_schema_ponto["financialInstitutions"] \
        .replace("{financialInstitutionId}", id)
    response = Ibanity.client.get(uri, {}, None)
    return __create_financial_institution_named_tuple__(response["data"])


def __create_financial_institution_named_tuple__(financial_institution):
    return namedtuple("FinancialInstitution", financial_institution.keys())(**financial_institution)
