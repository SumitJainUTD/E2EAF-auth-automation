from E2EAF_auth_automation.resources.configuration import Configuration
from E2EAF_common import ApiClient, DataError
from E2EAF_auth_automation.resources import auth_constants


class Auth:

    def __init__(self, env=None):
        self.env = env
        self.config = Configuration(env)
        self.api_client = ApiClient()

    def get_token(self, username, password):
        if (username is None) or (password is None):
            raise DataError("Require Username and password for login")

        url = self.config.base_uri + auth_constants.auth_uri
        body = {
            'username': username,
            'password': password
        }
        response = self.api_client.call_api(method="POST", url=url, data=body)
        return response

    def get_refresh_token(self, refresh_token):
        if refresh_token is None:
            raise DataError("refresh_token is None")

        url = self.config.base_uri + self.config.auth_uri + "refresh"
        body = {
            'refresh': refresh_token
        }
        response = self.api_client.call_api(method="POST", url=url, body=body)
        if response.status_code == 200:
            access_token = response.json()['access']
            refresh = response.json()['refresh']
            return response.json()
        elif response.status_code == 401:
            raise DataError("Invalid refresh token")
