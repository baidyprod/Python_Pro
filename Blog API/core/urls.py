from blog_api.views import CommentViewSet, PublicationViewSet

from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from rest_framework.authtoken import views


router = routers.DefaultRouter()
router.register(r'publications', PublicationViewSet, basename='publication')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.ObtainAuthToken.as_view()),
    path('', include(router.urls)),

]
