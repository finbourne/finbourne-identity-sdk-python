from unittest import TestCase
from finbourne_identity.utilities.config_keys import ConfigKeys


class TestConfigKeys(TestCase):
    def test_identity_url_in_config_keys(self):
        # Arrange
        expected_config_keys_subset = {
            "api_url": {"env": "FBN_LUSID_IDENTITY_URL", "config": "identityUrl"}
        }

        # Act
        actual_config_keys = ConfigKeys().get()

        # Assert
        self.assertEqual(
            actual_config_keys, expected_config_keys_subset | actual_config_keys
        )
