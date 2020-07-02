# pylint: disable=wrong-import-position

APP_NAME = "auth_service"
OPERATION_NAME = "user_sign_up"
REQUEST_METHOD = "post"
URL_SUFFIX = "user/sign_up/v1/"

from .test_case_01 import TestCase01UserSignUpAPITestCase

__all__ = [
    "TestCase01UserSignUpAPITestCase"
]
