# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.auth import SESSION_KEY
from django.test import TestCase

# Create your tests here.
class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'
        }
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # login
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in
        self.assertTrue(response.context['user'].is_active)

