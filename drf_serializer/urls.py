"""drf_serializer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from app01 import views

from rest_framework.documentation import include_docs_urls

from utils.docs import SwaggerSchemaView

# from rest_framework.schemas import get_schema_view
# from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
# schema_view = get_schema_view(title='API文档', renderer_classes=[SwaggerUIRenderer,OpenAPIRenderer])

urlpatterns = [
    # url(r'^docs/', schema_view),
    url(r'^admin/', admin.site.urls),
    url(r'^books/$', views.BooksView.as_view()),
    url(r'^books2/$', views.BooksView2.as_view()),
    url(r'^books/(?P<pk>\d+)$', views.BookView.as_view()),

    url(r'^app02/', include('app02.urls')),
    url(r'^app03/', include('app03.urls')),

    url(r'^docs/', include_docs_urls(title='文档'))
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^docs/', SwaggerSchemaView.as_view(), name='apiDocs'),

]
