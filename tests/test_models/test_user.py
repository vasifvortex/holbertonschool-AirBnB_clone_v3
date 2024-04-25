#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User
        self.user1 = User(first_name='Saleh',
                          last_name='Abbas',
                          email='Saleh@gmail.com',
                          password='&hdhdsa')

    def test_first_name(self):
        """ """
        self.assertEqual(type(self.user1.first_name), str)

    def test_last_name(self):
        """ """
        self.assertEqual(type(self.user1.last_name), str)

    def test_email(self):
        """ """
        self.assertEqual(type(self.user1.email), str)

    def test_password(self):
        """ """
        self.assertEqual(type(self.user1.password), str)