from django.conf.urls import url, include

from apps.employee.views import index

urlpatterns = [
    url(r'^$', index),
]
