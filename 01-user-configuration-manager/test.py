import unittest
from main import add_setting


class TestAddSetting(unittest.TestCase):
    def test_add_setting_stores_successfully(self):
        user_data = {}
        setting = ("theme", "dark")
        result = add_setting(user_data, setting)

        self.assertEqual(
            result, "Setting '[theme]' added with value '[dark]' successfully!"
        )
        self.assertIn("theme", user_data)
        self.assertEqual(user_data["theme"], "dark")

    def test_add_setting_ignores_existing_key(self):
        user_data = {"theme": "light"}
        setting = ("theme", "dark")
        result = add_setting(user_data, setting)

        self.assertEqual(
            result, "Setting '[theme]' already exists! Cannot add a new setting with this name."
        )
        self.assertIn("theme", user_data)
        self.assertEqual(user_data["theme"], "light")

    def test_add_setting_normalizes_key_to_lowercase(self):
        user_data = {}
        setting = ("THEME", "dark")
        result = add_setting(user_data, setting)

        self.assertEqual(
            result, "Setting '[theme]' added with value '[dark]' successfully!"
        )
        self.assertIn("theme", user_data)
        self.assertEqual(user_data["theme"], "dark")

    def test_add_setting_normalizes_value_to_lowercase(self):
        user_data = {}
        setting = ("theme", "DARK")
        result = add_setting(user_data, setting)

        self.assertEqual(
            result, "Setting '[theme]' added with value '[dark]' successfully!"
        )
        self.assertIn("theme", user_data)
        self.assertEqual(user_data["theme"], "dark")


if __name__ == "__main__":
    unittest.main()
