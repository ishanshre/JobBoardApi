"""
    Testing models in Authentication App
"""

from django.test import TestCase
from django.contrib.auth import get_user_model

from authentication.models import CompanyProfile, JobSeekerProfile

User = get_user_model()

class ModelTest(TestCase):
    def setUp(self):
        """Initializing test variables"""
        self.username = "test"
        self.email = "test@test.com"
        self.password = "password@123"
    
    def test_create_user_ok(self):
        """Test creating user is ok"""
        user = User.objects.create_user(
            username=self.username,
            email=self.email
        )
        user.set_password(self.password)
        self.assertEqual(user.username, self.username)
        self.assertEqual(user.email, self.email)
        self.assertTrue(user.check_password(self.password))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_company)
        self.assertFalse(user.is_job_seeker)
    
    def test_create_super_user_ok(self):
        """Testing create super ser"""
        user = User.objects.create_superuser(
            username=self.username,
            email=self.email
        )
        user.set_password(self.password)
        self.assertEqual(user.username, self.username)
        self.assertEqual(user.email, self.email)
        self.assertTrue(user.check_password(self.password))
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertFalse(user.is_company)
        self.assertFalse(user.is_job_seeker)
    

    def test_create_company_user_ok(self):
        """Testing create a company user"""
        user = User.objects.create_user(
            username=self.username,
            email=self.email,
            is_company=True
        )
        user.set_password(self.password)
        self.assertEqual(user.username, self.username)
        self.assertEqual(user.email, self.email)
        self.assertTrue(user.check_password(self.password))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_company)
        self.assertFalse(user.is_job_seeker)
    
    def test_create_job_seeker_user_ok(self):
        """Testing create a company user"""
        user = User.objects.create_user(
            username=self.username,
            email=self.email,
            is_job_seeker=True
        )
        user.set_password(self.password)
        self.assertEqual(user.username, self.username)
        self.assertEqual(user.email, self.email)
        self.assertTrue(user.check_password(self.password))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_company)
        self.assertTrue(user.is_job_seeker)
    

    def test_create_company_user_has_company_profile_only(self):
        """Testing creating company user has company profile only"""
        user = User.objects.create_user(
            username=self.username,
            email=self.email,
            is_company=True
        )
        user.set_password(self.password)
        self.assertEqual(user.username, self.username)
        self.assertEqual(user.email, self.email)
        self.assertTrue(user.check_password(self.password))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_company)
        self.assertFalse(user.is_job_seeker)
        profile = CompanyProfile.objects.get(user=user)
        self.assertEqual(user.id,profile.user.id)
        with self.assertRaises(JobSeekerProfile.DoesNotExist):
            JobSeekerProfile.objects.get(user=user)
    
    def test_create_job_seeker_user_has_job_profile_only(self):
        """Testing creating job seeker user has job seeker profile only"""
        user = User.objects.create_user(
            username=self.username,
            email=self.email,
            is_job_seeker=True
        )
        user.set_password(self.password)
        self.assertEqual(user.username, self.username)
        self.assertEqual(user.email, self.email)
        self.assertTrue(user.check_password(self.password))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_company)
        self.assertTrue(user.is_job_seeker)
        profile = JobSeekerProfile.objects.get(user=user)
        self.assertEqual(user.id,profile.user.id)
        with self.assertRaises(CompanyProfile.DoesNotExist):
            CompanyProfile.objects.get(user=user)
        