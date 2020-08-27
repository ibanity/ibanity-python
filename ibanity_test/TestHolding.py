from ibanity import Ibanity
from ibanity.api import Xs2a
from ibanity.api import Sandbox
from ibanity.api import PontoConnect
import unittest
import os
import environ
import uuid

class TestHolding(unittest.TestCase):

	def test_holding(self):
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
		fi_account_id = fi_account["id"]
		cat = Xs2a.CustomerAccessToken.create("15874569")
		cat = cat["token"]
		aiar_info = {"redirectUri" : "http://localhost:3000/account-information-access-request-confirmations", "consentReference" : str(uuid.uuid1()), "allowFinancialInstitutionRedirectUri" : False, "skipIbanityCompletionCallback" : False}
		aiar = Xs2a.AccountInformationAccessRequest.create(fi_id, cat, aiar_info)
		aiar_id = aiar["id"]
		redirect = aiar["redirect"]
		authCommand = "run ibanity/sandbox-authorization-cli:latest account-information-access -f " + fi_id + " -l " + "USERLOGIN_1" + " -p password -a " + "BE452784012" + "#EUR" + " -r " + redirect
		cli = os.system("docker " + authCommand)
		account_list = Xs2a.Account.get_list(cat)
		self.assertEqual(len(account_list), 1)
		account_id = account_list[0]["id"]
		holding_list = Xs2a.Holding.get_list(fi_id, account_id, cat)
		fi_account_delete = Sandbox.FinancialInstitutionAccount.delete(fi_id, fi_user_id, fi_account_id)
		fi_user_delete = Sandbox.FinancialInstitutionUser.delete(fi_user_id)
		fi_delete = Xs2a.FinancialInstitution.delete(fi_id)


if __name__ == '__main__':
    unittest.main()