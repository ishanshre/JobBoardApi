"""
Testing API in authentication app
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


User = get_user_model()
CREATE_USER_URL = reverse("authentication:register")

def create_user(**params):
    """Create and return new user"""
    return User.objects.create_user(**params)



class AuthenticationAppApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.payload = {
            "username":"heloooo",
            "password":"test@123",
            "email":"test@gmail.com",          
        }
        self.payload1 = {
            "username":"heloooo",
            "password":"test@123",
            "confirm_password":"test@123",
            "email":"test@gmail.com",
            "is_company":True            
        }
        self.payload2 = {
            "username":"heloooo",
            "password":"test@123",
            "confirm_password":"test@123",
            "email":"test@gmail.com",
            "is_job_seeker":True            
        }
    
    def test_register_user_as_company(self):
        """Testing user api create user as a company success"""
        self.assertEqual(self.payload1["password"], self.payload1["confirm_password"])
        res = self.client.post(CREATE_USER_URL, self.payload1)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(username=self.payload1["username"])
        self.assertEqual(user.email, self.payload1['email'])
        self.assertTrue(user.is_company)
        self.assertFalse(user.is_job_seeker)
    
    def test_register_user_as_a_job_seeker(self):
        """Testing user api create user as a job seeker"""
        self.assertEqual(self.payload2["password"], self.payload2["confirm_password"])
        res = self.client.post(CREATE_USER_URL, self.payload2)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(username=self.payload2["username"])
        self.assertEqual(user.email, self.payload2['email'])
        self.assertFalse(user.is_company)
        self.assertTrue(user.is_job_seeker)