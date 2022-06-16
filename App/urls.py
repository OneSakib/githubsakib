from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# Create Router for the api links
router = DefaultRouter()
router.register(r'student', views.StudentViewSet)
router.register(r'group', views.GroupViewSet)

app_name = 'App'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework'))
]
