from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Organization, Membership,Course
class TenantIsolationTests(TestCase):
    def setUp(self):
        self.a=Organization.objects.create(name='School A')
        self.b=Organization.objects.create(name='School B')
        self.user=get_user_model().objects.create_user(username='testuser',password='local-test-only-strong-pass')
        Membership.objects.create(organization=self.a,user=self.user,role='teacher')
        Course.objects.create(organization=self.a,title='Class A')
        Course.objects.create(organization=self.b,title='Class B')
        self.client=APIClient()
        self.client.force_authenticate(user=self.user)
    def test_cannot_read_other_school_courses(self):
        r=self.client.get(f'/api/organizations/{self.b.id}/courses/')
        self.assertEqual(r.status_code,404)
    def test_can_read_own_school_courses(self):
        r=self.client.get(f'/api/organizations/{self.a.id}/courses/')
        self.assertEqual(r.status_code,200)
        self.assertEqual(len(r.json()['courses']),1)
