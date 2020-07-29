from collections import namedtuple
from ibanity import Ibanity

def delete(customer_access_token):
    uri = Ibanity.client.api_schema["customer"]["self"]
    response = Ibanity.client.delete(uri, {}, None)
    return __create_customer_named_tuple__(response["data"])


def __create_customer_named_tuple__(customer):
    return namedtuple("FinancialInstitutioncustomer", customer.keys())(**customer)
