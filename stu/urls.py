from django.conf.urls import url

from stu import views

urlpatterns = [
    url(r'^stu/$', views.Register.as_view()),
]
