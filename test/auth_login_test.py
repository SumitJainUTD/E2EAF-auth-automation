import os
import pytest
from .auth_helper import AuthHelper
from E2EAF_auth_automation.auth.auth import Auth
import logging

env = os.environ.get('env')
if os.environ.get('env') is not None:
    env = os.environ.get('env')
else:
    env = 'qa'

logger = logging.getLogger(__name__)
logger.setLevel('INFO')

auth = Auth(env)
authHelper = AuthHelper(env, auth)



@pytest.mark.parametrize(
    "test_case, username, password, successfully_login",  [
        ('valid_login_test', 'test', 'test', True),
        # ('invalid_login_test', 'test', 'invalid', False),
    ])
def test_login_feature(test_context, test_case, username, password, successfully_login):
    logger.info("************** Start Test: " +test_case+ " ***********")
    result = True
    response = authHelper.login(username=username, password=password)
    if successfully_login:
        if response.status_code == 200:
            logging.info("successfully login")
        else:
            logger.info("Unable to login, response code: " + response.status_code)
            result &= False
    else:
        if response.status_code == 401:
            logger.info("Unable to login with invalid credentials")
        else:
            logger.info("Logged in using invalid credentials, response code: " + response.status_code)
            result &= False
    assert result
    logger.info("************** End Test ***********")
