from unittest import TestCase
from authentication.authentication_helpers import UserBasicData, AuthenticationManager
from test_helpers.helpers import wipe_database
from infrastructure.redis import db
class TestAuthenticationManager(TestCase):
    _user1 = UserBasicData("mb@gmail.com", "StrongPassword123#")
    _user2 = UserBasicData("mb1@gmail.com", "StrongPassword1234#")
    _user3 = UserBasicData("mb1@gmail.com", "StrongPassword1234sadsa#")

    def setUp(self):
        wipe_database(db)
        self.manager = AuthenticationManager()


    def test_get_user_by_email_when_user_exists(self):
        """Should return UserBasicData instance if user was stored properly"""
        self.manager.save_user(self._user1)
        retrivered_user_1 = self.manager.get_user_by_email(self._user1.get_mail())
        assert retrivered_user_1 is not None
        assert retrivered_user_1.get_mail() == self._user1.get_mail()

    def test_get_user_by_email_when_user_is_not_present(self):
        """Should return None if user does not exists"""
        retrivered_user_1 = self.manager.get_user_by_email("nonextisting@wp.pl")
        assert retrivered_user_1 is None

    def test_save_user(self):
        """ Should save users"""
        # given
        # when
        self.manager.save_user(self._user1)
        self.manager.save_user(self._user2)
        self.manager.save_user(self._user3)
        # then
        retrivered_user_1 = self.manager.get_user_by_email(self._user1.get_mail())
        assert retrivered_user_1.get_mail() == self._user1.get_mail()

    def test_verify_pass_for_user(self):
        # given
        self.manager.save_user(self._user1)
        # when then
        assert self.manager.verify_pass_for_user(self._user1.get_mail(), "StrongPassword123#")
        assert not self.manager.verify_pass_for_user(self._user1.get_mail(), "wrongPASS")
