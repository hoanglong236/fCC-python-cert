def add_setting(user_data, setting):
    k, v = setting
    k, v = k.lower(), v.lower()
    if k in user_data:
        return f"Setting '{k}' already exists! Cannot add a new setting with this name."
    user_data[k] = v
    return f"Setting '{k}' added with value '{v}' successfully!"

def update_setting(user_data, setting):
    k, v = setting
    k, v = k.lower(), v.lower()
    if k in user_data:
        user_data[k] = v
        return f"Setting '{k}' updated to '{v}' successfully!"
    return f"Setting '{k}' does not exist! Cannot update a non-existing setting."

def delete_setting(user_data, key):
    key = key.lower()
    if key in user_data:
        del user_data[key]
        return f"Setting '{key}' deleted successfully!"
    return f"Setting not found!"

def view_settings(user_data):
    if not len(user_data):
        return "No settings available."
    settings = [f"{k.capitalize()}: {v}" for k, v in user_data.items()]
    s = '\n'.join(settings)
    return f"Current User Settings:\n{s}\n"

test_settings = {
    "theme": "dark",
    "font": "arial"
}
