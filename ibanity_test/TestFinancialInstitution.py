from ibanity import Ibanity
from ibanity.api import Xs2a
from ibanity.api import Sandbox
from ibanity.api import PontoConnect
import unittest
import environ

class TestFinancialInstitution(unittest.TestCase):

	def test_financial_institution(self):
		env = environ.Env()
		environ.Env.read_env()
		obj = Ibanity(env('IBANITY_CERTIFICATE_PATH'), env('IBANITY_PRIVATE_KEY_PATH'), env('IBANITY_PASSPHRASE'), "api.ibanity.com")
		finame = {'name' : 'The Bank'}
		ficreate = Xs2a.FinancialInstitution.create(finame)
		fi_id = ficreate["id"]
		fi_find = Xs2a.FinancialInstitution.find(fi_id)
		filist = Xs2a.FinancialInstitution.get_list()
		self.assertEqual(len(filist), 1)
		fi_delete = Xs2a.FinancialInstitution.delete(fi_id)


if __name__ == '__main__':
    unittest.main()