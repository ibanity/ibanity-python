from collections import namedtuple


def get_list(client, params):
    uri = client.api_schema["financialInstitutions"].replace("{financialInstitutionId}", "")
    response = client.get(uri, params, None)
    return list(
        map(
            lambda financial_institution:
            __create_financial_institution_named_tuple__(financial_institution), response["data"]
        )
    )

def find(client, id):
    uri = client.api_schema["financialInstitutions"].replace("{financialInstitutionId}", id)
    response = client.get(uri, {}, None)
    return __create_financial_institution_named_tuple__(response["data"])

def __create_financial_institution_named_tuple__(financial_institution):
    return namedtuple("FinancialInstitution", financial_institution.keys())(**financial_institution)
