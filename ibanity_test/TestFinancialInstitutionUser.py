from ibanity import Ibanity
from ibanity.api import Xs2a
from ibanity.api import Sandbox
from ibanity.api import PontoConnect
import unittest
import environ

class TestFinancialInstitutionUser(unittest.TestCase):

	def test_financial_institution_user(self):
		env = environ.Env()
		environ.Env.read_env()
		obj = Ibanity(env('IBANITY_CERTIFICATE_PATH'), env('IBANITY_PRIVATE_KEY_PATH'), env('IBANITY_PASSPHRASE'), "api.ibanity.com")
		user_info = {"login" : "USERLOGIN_1", "password" : "password", "firstName" : "first", "lastName" : "last"}
		fi_user = Sandbox.FinancialInstitutionUser.create(user_info)
		fi_user_id = fi_user["id"]
		user_find = Sandbox.FinancialInstitutionUser.find(fi_user_id)
		fi_user_list = Sandbox.FinancialInstitutionUser.get_list()
		self.assertEqual(len(fi_user_list), 1)
		fi_user_delete = Sandbox.FinancialInstitutionUser.delete(fi_user_id)


if __name__ == '__main__':
    unittest.main()