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

		transaction_info = {"valueDate" : "2017-05-22", "executionDate" : "2017-05-25", "amount" : 84.42, "currency" : "EUR", "counterpartName" : "The Bank", "counterpartReference" : "BE9786154282054", "description" : "Small Cotton Shoes", "remittanceInformation" : "NEW SHOES", "remittanceInformationType" : "unstructured"}
		fi_transaction = Sandbox.FinancialInstitutionTransaction.create(fi_id, fi_user_id, fi_account_id, transaction_info)
		fi_transaction_list = Sandbox.FinancialInstitutionTransaction.get_list(fi_id, fi_user_id, fi_account_id)
		self.assertEqual(len(fi_transaction_list), 1)
		fi_transaction_id = fi_transaction["id"]
		fi_transaction_find = Sandbox.FinancialInstitutionTransaction.find(fi_id, fi_user_id, fi_account_id, fi_transaction_id)
		fi_transaction_delete = Sandbox.FinancialInstitutionTransaction.delete(fi_id, fi_user_id, fi_account_id, fi_transaction_id)

		fi_account_delete = Sandbox.FinancialInstitutionAccount.delete(fi_id, fi_user_id, fi_account_id)
		fi_user_delete = Sandbox.FinancialInstitutionUser.delete(fi_user_id)
		fi_delete = Xs2a.FinancialInstitution.delete(fi_id)


if __name__ == '__main__':
    unittest.main()