import unittest
from finbourne_identity import api as iapi
from finbourne_identity.utilities import ApiClientFactory

class IdentityTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        api_client_factory = ApiClientFactory()
        cls.users_api = api_client_factory.build(iapi.UsersApi)
        cls.roles_iapi = api_client_factory.build(iapi.RolesApi)

    def test_roles_are_returned_when_calling_list_roles(self):
        identity_roles = self.roles_iapi.list_roles()
        self.assertIsNotNone(identity_roles)
        self.assertIsNot(identity_roles, str)

    def test_users_are_returned_when_calling_list_users(self):
        user_list = self.users_api.list_users()
        self.assertGreater(len(user_list), 0)


if __name__ == '__main__':
    unittest.main()
