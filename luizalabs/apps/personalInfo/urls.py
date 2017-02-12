from django.conf.urls import url

from apps.personalInfo.views import index_personal

urlpatterns = [
  url(r'^$', index_personal),
]
