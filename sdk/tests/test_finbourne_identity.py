import unittest
from finbourne_identity import ApiClientBuilder as identity_api
from finbourne_identity import api as iapi
from lusidjam import RefreshingToken
from finbourne_identity.utilities import ApiClientFactory

class Lydia(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lusid_api_factory = ApiClientFactory(token=RefreshingToken(),
                                                             api_secrets_filename="secrets.json")
        api_client = lusid_api_factory.api_client
        identity_api_client = identity_api.build(api_secrets_filename="secrets.json",
                                                 token=api_client.configuration.access_token)
        cls.users_api = iapi.UsersApi(identity_api_client)
        cls.roles_iapi = iapi.RolesApi(identity_api_client)

    def test_roles(self):
        identity_roles = self.roles_iapi.list_roles()
        self.assertIsNotNone(identity_roles)
        self.assertEqual(type(identity_roles[0].to_dict()['description']), str)
        self.assertIsNot(identity_roles, str)

    def test_users(self):
        user_list = self.users_api.list_users()
        self.assertIsNotNone(user_list[0].to_dict()['id'])


if __name__ == '__main__':
    unittest.main()
