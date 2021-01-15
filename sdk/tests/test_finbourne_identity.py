import unittest
from finbourne_identity import api as la, ApiClientBuilder
from finbourne_identity.utilities import ApiClientFactory

api_client = ApiClientFactory()
domains_api = api_client.build(la.DomainsApi)

class Lydia(unittest.TestCase):

    def test_policies(self):
        domain = domains_api.get_my_domain()
        self.assertIsNotNone(domain)


if __name__ == '__main__':
    unittest.main()
