from E2EAF_auth_automation.auth.auth import Auth
from E2EAF_common.exceptions import DataError


class AuthHelper():
    def __init__(self, env=None, auth=None):
        self.env = env
        self.auth = auth

    def login(self, username, password):
        if (username is None) or (password is None):
            raise DataError("Require Username and password for login")

        response = self.auth.get_token(username=username, password=password)

        if response.status_code == 200:
            access_token = response.json()['access']
            refresh = response.json()['refresh']
            return response
        elif response.status_code == 401:
            raise DataError("Invalid username or password")