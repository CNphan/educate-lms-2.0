from django.contrib import admin
from django.urls import path
from core.views import health, organizations, courses
urlpatterns=[path('admin/',admin.site.urls),path('health/',health),path('api/organizations/',organizations),path('api/organizations/<uuid:organization_id>/courses/',courses)]
