from ibanity import Ibanity
from ibanity.api import Xs2a
from ibanity.api import Sandbox
from ibanity.api import PontoConnect
import unittest
import environ

class TestFinancialInstitutionHolding(unittest.TestCase):

	def test_financial_institution_name(self):
		env = environ.Env()
		environ.Env.read_env()
		obj = Ibanity(env('IBANITY_CERTIFICATE_PATH'), env('IBANITY_PRIVATE_KEY_PATH'), env('IBANITY_PASSPHRASE'), "api.ibanity.com")
		finame = {'name' : 'The Bank'}
		fi = Xs2a.FinancialInstitution.create(finame)
		fi_id = fi["id"]
		user_info = {"login" : "USERLOGIN_1", "password" : "password", "firstName" : "first", "lastName" : "last"}
		fi_user = Sandbox.FinancialInstitutionUser.create(user_info)
		fi_user_id = fi_user["id"]
		account_info = {"subtype" : "checking", "reference" : "BE452784012", "referenceType" : "IBAN", "description" : "Savings account", "currency" : "EUR"}
		fi_account = Sandbox.FinancialInstitutionAccount.create(fi_id, fi_user_id, account_info)
		fi_account_list = Sandbox.FinancialInstitutionAccount.get_list_for_financial_institution(fi_id, fi_user_id)
		fi_account_id = fi_account["id"]
		fi_account_find = Sandbox.FinancialInstitutionAccount.find(fi_id, fi_user_id, fi_account_id)

		holding_info = {"name" : "AAPL", "subtype" : "STOCK", "reference" : "US0378331003", "referenceType" : "ISIN", "quantity" : 10, "lastValuationDate" : "2020-01-01", "lastValuationCurrency" : "EUR", "lastValuation" : 155.5, "totalValuation" : 1555, "totalValuationCurrency" : "EUR"}
		fi_holding = Sandbox.FinancialInstitutionHolding.create(fi_id, fi_user_id, fi_account_id, holding_info)
		fi_holding_list = Sandbox.FinancialInstitutionHolding.get_list(fi_id, fi_user_id, fi_account_id)
		self.assertEqual(len(fi_holding_list), 1)
		fi_holding_id = fi_holding["id"]
		fi_holding_find = Sandbox.FinancialInstitutionHolding.find(fi_id, fi_user_id, fi_account_id, fi_holding_id)
		fi_holding_delete = Sandbox.FinancialInstitutionHolding.delete(fi_id, fi_user_id, fi_account_id, fi_holding_id)

		fi_account_delete = Sandbox.FinancialInstitutionAccount.delete(fi_id, fi_user_id, fi_account_id)
		fi_user_delete = Sandbox.FinancialInstitutionUser.delete(fi_user_id)
		fi_delete = Xs2a.FinancialInstitution.delete(fi_id)


if __name__ == '__main__':
    unittest.main()