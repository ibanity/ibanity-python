from ibanity import Ibanity
from ibanity.api import Xs2a
from ibanity.api import Sandbox
from ibanity.api import PontoConnect
import unittest
import os
import environ
import base64

class TestPontoConnect(unittest.TestCase):

	def test_ponto_connect(self):
		env = environ.Env()
		environ.Env.read_env()
		obj = Ibanity(env('IBANITY_CERTIFICATE_PATH'), env('IBANITY_PRIVATE_KEY_PATH'), env('IBANITY_PASSPHRASE'), "api.ibanity.com")
		ponto_fi_list = PontoConnect.FinancialInstitution.get_list()
		self.assertEqual(len(ponto_fi_list), 3)
		ponto_fi_id = ponto_fi_list[0]["id"]
		ponto_fi_find = PontoConnect.FinancialInstitution.find(ponto_fi_id)
		a = env('PONTO_CONNECT_CLIENT_ID') + ':' + env('PONTO_CONNECT_CLIENT_SECRET')
		auth_encode = base64.b64encode(a.encode("ascii"))
		auth = auth_encode.decode("ascii")
		token = PontoConnect.Token.create("Hn4X9OCYMqkMqv4EYS9Jr8PU11bLyCZ9ukZyorEwDss.qslW1tX-JzEB07niF6ml-765aoRbH0SXWOEmGgvg77o", "edf6f4bb2f02d8fdf8f58a1aff4076144d6632f9204dd5ab", "http://localhost:3000/ponto_tokens/new", env('PONTO_CONNECT_CLIENT_ID'), auth)
		token = PontoConnect.Token.create_from_refresh_token(token["refresh_token"], env('PONTO_CONNECT_CLIENT_ID'), auth)
		self.assertEqual(len(token["access_token"]), 87)
		ponto_account_list = PontoConnect.Account.get_list(token["access_token"])
		self.assertEqual(len(ponto_account_list), 3)
		ponto_account_id = ponto_account_list[0]["id"]
		ponto_account_find = PontoConnect.Account.find(ponto_account_id, token["access_token"])
		payment_info = {"remittanceInformation" : "payment", "remittanceInformationType" : "unstructured", "currency" : "EUR", "amount" : 59, "creditorName" : "Alex Cred", "creditorAccountReference" : "BE55732022998044", "creditorAccountReferenceType" : "IBAN", "creditorAgent" : "NBBEBEBB204", "creditorAgentType" : "BIC"}
		ponto_payment = PontoConnect.Payment.create(ponto_account_id, payment_info, token["access_token"])
		self.assertEqual(ponto_payment["type"], "payment")
		ponto_payment_id = ponto_payment["id"]
		ponto_payment_find = PontoConnect.Payment.find(ponto_account_id, ponto_payment_id, token["access_token"])
		ponto_payment_del = PontoConnect.Payment.delete(ponto_account_id, ponto_payment_id, token["access_token"])
		ponto_transaction_list = PontoConnect.Transaction.get_list(ponto_account_id, token["access_token"])
		self.assertEqual(len(ponto_transaction_list), 10)
		ponto_transaction_id = ponto_transaction_list[0]["id"]
		ponto_transaction_find = PontoConnect.Transaction.find(ponto_account_id, ponto_transaction_id, token["access_token"])
		# sync_info = {"resourceType" : "account", "resourceId" : ponto_account_id, "subtype" : "accountDetails"}
		# ponto_sync = PontoConnect.Synchronization.create(sync_info, token["access_token"])
		# ponto_sync_find = PontoConnect.Synchronization.find(ponto_sync["id"], token["access_token"])


if __name__ == '__main__':
    unittest.main()