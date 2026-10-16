import uuid
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [
        migrations.CreateModel(name='Organization', fields=[
            ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, serialize=False)),
            ('name', models.CharField(max_length=200)),
            ('created_at', models.DateTimeField(auto_now_add=True)),
        ]),
        migrations.CreateModel(name='Course', fields=[
            ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, serialize=False)),
            ('title', models.CharField(max_length=200)),
            ('created_at', models.DateTimeField(auto_now_add=True)),
            ('organization', models.ForeignKey(to='core.organization', on_delete=django.db.models.deletion.CASCADE)),
        ]),
        migrations.CreateModel(name='Membership', fields=[
            ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ('role', models.CharField(max_length=20, choices=[('admin','Admin'),('teacher','Teacher'),('student','Student')])),
            ('organization', models.ForeignKey(to='core.organization', on_delete=django.db.models.deletion.CASCADE)),
            ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.CASCADE)),
        ]),
        migrations.CreateModel(name='Enrollment', fields=[
            ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ('course', models.ForeignKey(to='core.course', on_delete=django.db.models.deletion.CASCADE)),
            ('student', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.CASCADE)),
        ]),
        migrations.AddConstraint(model_name='membership', constraint=models.UniqueConstraint(fields=('organization','user'), name='unique_school_membership')),
        migrations.AddConstraint(model_name='enrollment', constraint=models.UniqueConstraint(fields=('course','student'), name='unique_course_enrollment')),
    ]
