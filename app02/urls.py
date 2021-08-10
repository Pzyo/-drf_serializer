
from django.conf.urls import url
from app02 import views

urlpatterns = [
    url(r'^books/(?P<pk>\d+)$', views.APP02BookView.as_view()),
]