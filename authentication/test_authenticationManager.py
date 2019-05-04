from unittest import TestCase
from authentication.authentication_helpers import UserBasicData


class TestAuthenticationManager(TestCase):
    _user1 = UserBasicData("mb@gmail.com", "StrongPassword123#")
    _user2 = UserBasicData("mb1@gmail.com", "StrongPassword1234#")
    _user3 = UserBasicData("mb1@gmail.com", "StrongPassword1234sadsa#")

    def setUp(self):
        pass

    def test_get_user_by_email_when_user_exists(self):
        """Should return UserBasicData instance if user was stored properly"""
        self.fail()

    def test_get_user_by_email_when_user_is_not_present(self):
        """Should return None if user does not exists"""
        self.fail()

    def test_save_user(self):
        # given
        user = UserBasicData("mb@gmail.com", "StrongPassword123#")

        self.fail()

    def test_verify_pass_for_user(self):
        self.fail()
