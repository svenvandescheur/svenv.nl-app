from blog.views import *
from django.conf import settings
from django.conf.urls import patterns, include, url
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'search/posts', SearchPostViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(settings.CONTACT_PAGE_PATH, ContactView.as_view(), name='contact'),
    url(r'^sitemap.xml$', SiteMapView.as_view(), name='sitemap'),

    url(r'^(?P<page_path>[a-zA-Z0-9-_]+)$', PageView.as_view(), name='page'),

    url(r'^(?P<category_name>)$', CategoryView.as_view(), name='home'),
    url(r'^(?P<category_name>[a-zA-Z0-9-_]+)?/$', CategoryView.as_view(), name='category'),
    url(r'^(?P<category_name>[a-zA-Z0-9-_]+)/(?P<short_title>[a-zA-Z0-9-_]+)$', PostView.as_view(),  name='post'),
]
