import uuid
from django.conf import settings
from django.db import models
class Organization(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
class Membership(models.Model):
    organization=models.ForeignKey(Organization,on_delete=models.CASCADE)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    role=models.CharField(max_length=20,choices=[('admin','Admin'),('teacher','Teacher'),('student','Student')])
    class Meta:
        constraints=[models.UniqueConstraint(fields=['organization','user'],name='unique_school_membership')]
class Course(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    organization=models.ForeignKey(Organization,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
class Enrollment(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    student=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    class Meta:
        constraints=[models.UniqueConstraint(fields=['course','student'],name='unique_course_enrollment')]
