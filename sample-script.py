import os

# Specify the environment variable name
env_var_name = "MY_ENV_VAR"

# Retrieve the environment variable
env_value = os.getenv(env_var_name)

# Output the value
if env_value:
    print(f"The value of {env_var_name} is: {env_value}")
else:
    print(f"{env_var_name} is not set in the environment.")
