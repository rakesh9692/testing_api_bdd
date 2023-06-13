# -*- coding: UTF-8 -*-
import os

def get_from_env(env_var_name, backup_value):
    return backup_value if os.getenv(env_var_name) is None else os.getenv(env_var_name)

def before_all(context):
    context.base_url = get_from_env("BASE_URI", "https://api.tmsandbox.co.nz")
