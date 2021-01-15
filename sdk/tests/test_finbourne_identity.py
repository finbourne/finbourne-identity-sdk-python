import unittest
from finbourne_identity import api as la, ApiClientBuilder
from finbourne_identity.utilities import ApiClientFactory


class Lydia(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        api_client = ApiClientFactory()
        cls.domains_api = api_client.build(la.DomainsApi)

    def test_policies(self):
        domain = self.domains_api.get_my_domain()
        self.assertIsNotNone(domain)

if __name__ == '__main__':
    unittest.main()
