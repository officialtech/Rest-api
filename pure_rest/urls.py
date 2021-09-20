
from django.urls.conf import path, include
from rest_framework import routers
from pure_rest.views import BookView, PublisherView, AuthorView
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register('books', viewset=BookView)
router.register('authors', viewset=AuthorView)
router.register('publishers', viewset=PublisherView)

urlpatterns = [
    path('', include(router.urls)),
    path('get-api-token/', views.obtain_auth_token, name="api_token"),
]
