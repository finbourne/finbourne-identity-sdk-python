import unittest
from finbourne_identity import api as la, ApiClientBuilder


class Lydia(unittest.TestCase):

    def test_policies(self):
        api_client = ApiClientBuilder().build("secrets.json")
        domains_api = la.DomainsApi(api_client)

        domain = domains_api.get_my_domain()

        self.assertIsNotNone(domain)


if __name__ == '__main__':
    unittest.main()
