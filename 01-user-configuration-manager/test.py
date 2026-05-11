import unittest
from main import add_setting, delete_setting, update_setting, view_settings


class TestAddSetting(unittest.TestCase):
    def test_add_setting_stores_successfully(self):
        user_data = {}
        setting = ("theme", "dark")
        result = add_setting(user_data, setting)

        self.assertEqual(
            result, "Setting 'theme' added with value 'dark' successfully!"
        )
        self.assertEqual(user_data.get("theme"), "dark")

    def test_add_setting_ignores_existing_key(self):
        user_data = {"theme": "light"}
        setting = ("theme", "dark")
        result = add_setting(user_data, setting)

        self.assertEqual(
            result, "Setting 'theme' already exists! Cannot add a new setting with this name."
        )
        self.assertEqual(user_data.get("theme"), "light")

    def test_add_setting_ignores_existing_key_case_insensitive(self):
        user_data = {"theme": "light"}
        setting = ("THEME", "dark")
        result = add_setting(user_data, setting)

        self.assertEqual(
            result, "Setting 'theme' already exists! Cannot add a new setting with this name."
        )
        self.assertEqual(user_data.get("theme"), "light")

    def test_add_setting_normalizes_key_to_lowercase(self):
        user_data = {}
        setting = ("THEME", "dark")
        result = add_setting(user_data, setting)

        self.assertEqual(
            result, "Setting 'theme' added with value 'dark' successfully!"
        )
        self.assertEqual(user_data.get("theme"), "dark")

    def test_add_setting_normalizes_value_to_lowercase(self):
        user_data = {}
        setting = ("theme", "DARK")
        result = add_setting(user_data, setting)

        self.assertEqual(
            result, "Setting 'theme' added with value 'dark' successfully!"
        )
        self.assertEqual(user_data.get("theme"), "dark")

    def test_update_setting_overwrite_existing_value(self):
        user_data = {"theme": "light"}
        setting = ("theme", "dark")
        result = update_setting(user_data, setting)

        self.assertEqual(result, "Setting 'theme' updated to 'dark' successfully!")
        self.assertEqual(user_data.get("theme"), "dark")

    def test_update_setting_not_update_if_key_not_exists(self):
        user_data = {"theme": "light"}
        setting = ("font", "arial")
        result = update_setting(user_data, setting)

        self.assertEqual(
            result, "Setting 'font' does not exist! Cannot update a non-existing setting."
        )
        self.assertIsNone(user_data.get("font"))

    def test_update_setting_normalizes_key_to_lowercase(self):
        user_data = {"theme": "light"}
        setting = ("THEME", "dark")
        result = update_setting(user_data, setting)

        self.assertEqual(result, "Setting 'theme' updated to 'dark' successfully!")
        self.assertNotIn("THEME", user_data)
        self.assertEqual(user_data.get("theme"), "dark")

    def test_update_setting_normalizes_value_to_lowercase(self):
        user_data = {"theme": "light"}
        setting = ("theme", "DARK")
        result = update_setting(user_data, setting)

        self.assertEqual(result, "Setting 'theme' updated to 'dark' successfully!")
        self.assertEqual(user_data.get("theme"), "dark")

    def test_update_setting_does_not_modify_other_settings(self):
        user_data = {"theme": "light", "font": "arial"}
        setting = ("theme", "dark")
        result = update_setting(user_data, setting)

        self.assertEqual(result, "Setting 'theme' updated to 'dark' successfully!")
        self.assertEqual(user_data.get("theme"), "dark")
        self.assertEqual(user_data.get("font"), "arial")

    def test_delete_setting_removes_existing_key(self):
        user_data = {"theme": "light"}
        key = "theme"
        result = delete_setting(user_data, key)

        self.assertEqual(result, "Setting 'theme' deleted successfully!")
        self.assertNotIn("theme", user_data)

    def test_delete_setting_not_delete_if_key_not_exists(self):
        user_data = {"theme": "light"}
        key = "font"
        result = delete_setting(user_data, key)

        self.assertEqual(result, "Setting not found!")

    def test_delete_setting_normalizes_key_to_lowercase(self):
        user_data = {"theme": "light"}
        key = "THEME"
        result = delete_setting(user_data, key)

        self.assertEqual(result, "Setting 'theme' deleted successfully!")
        self.assertNotIn("theme", user_data)

    def test_delete_setting_does_not_modify_other_settings(self):
        user_data = {"theme": "light", "font": "arial"}
        key = "theme"
        result = delete_setting(user_data, key)

        self.assertEqual(result, "Setting 'theme' deleted successfully!")
        self.assertIn("font", user_data)

    def test_view_settings_returns_all_settings(self):
        user_data = {"theme": "light", "font": "arial"}
        expected_output = "Current User Settings:\nTheme: light\nFont: arial\n"
        result = view_settings(user_data)

        self.assertEqual(result, expected_output)

    def test_view_settings_returns_no_settings_message(self):
        user_data = {}
        expected_output = "No settings available."
        result = view_settings(user_data)

        self.assertEqual(result, expected_output)

    def test_view_settings_does_not_modify_user_data(self):
        user_data = {"theme": "light", "font": "arial"}
        _ = view_settings(user_data)

        self.assertEqual(user_data, {"theme": "light", "font": "arial"})

    def test_view_settings_formats_output_correctly(self):
        user_data = {"theme": "light", "font": "arial"}
        expected_output = "Current User Settings:\nTheme: light\nFont: arial\n"
        result = view_settings(user_data)

        self.assertEqual(result, expected_output)

    def test_view_settings_handles_empty_values(self):
        user_data = {"theme": "light", "font": "" }
        expected_output = (
            "Current User Settings:\nTheme: light\nFont: \n"
        )
        result = view_settings(user_data)

        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()
