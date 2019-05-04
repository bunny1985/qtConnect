from unittest import TestCase
from authentication.authentication_helpers import UserBasicData, AuthenticationManager, _verify_password


class TestAuthenticationManager(TestCase):
    _user1 = UserBasicData("mb@gmail.com", "StrongPassword123#")
    _user2 = UserBasicData("mb1@gmail.com", "StrongPassword1234#")
    _user3 = UserBasicData("mb1@gmail.com", "StrongPassword1234sadsa#")

    def setUp(self):
        self.manager = AuthenticationManager()

    def test_get_user_by_email_when_user_exists(self):
        """Should return UserBasicData instance if user was stored properly"""
        self.fail()

    def test_get_user_by_email_when_user_is_not_present(self):
        """Should return None if user does not exists"""
        self.fail()

    def test_save_user(self):
        # given
        # when
        self.manager.save_user(self._user1)
        self.manager.save_user(self._user2)
        self.manager.save_user(self._user3)
        # then
        retrivered_user_1 = self.manager.get_user_by_email(self._user1.get_mail())
        assert retrivered_user_1.get_mail() == self._user1.get_mail()
        assert _verify_password(retrivered_user_1.get_password(), "StrongPassword123#")


    def test_verify_pass_for_user(self):
        self.fail()
