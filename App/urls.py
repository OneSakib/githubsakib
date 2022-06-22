from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.sitemaps.views import sitemap
from django.contrib import sitemaps
from rest_framework import renderers
from rest_framework.authtoken import views as DRFView

# Create Router for the api links
router = DefaultRouter()
router.register(r'student', views.StudentViewSet)
router.register(r'group', views.GroupViewSet)
# router.register(r'snippet', views.SnippetView)
# router.register(r'snippet/<int:pk>', views.SnippetDetailView)

app_name = 'App'

snippet_list = views.SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = views.SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = views.SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = views.UserViewSet.as_view({
    'get': 'list'
})
user_detail = views.UserViewSet.as_view({
    'get': 'retrieve'
})
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    # path('api/', include(router.urls)),
    path('snippet/', views.SnippetView.as_view(), name='snippet'),
    path('snippet/<int:pk>/', views.SnippetDetailView.as_view(), name='snippetdetail'),
    path('snippetmixin/', views.SnippetMixinView.as_view(), name='snippetgeneric'),
    path('snippetmixin/<int:pk>/', views.SnippetMixinDetailView.as_view(), name='snippetmixindetil'),
    path('snippetgeneric/', views.SnippetGeneric.as_view(), name='snippet-generic'),
    path('snippetgeneric/<int:pk>/', views.SnipperGenericDetail.as_view(), name='geneicdetail'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='userdetail'),
    path('api-root/', views.api_root),
    path('snippetgeneric/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippethighlight'),
    path('snippetsviewset/', snippet_list, name='snippet-list'),
    path('snippetsviewset/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippetsviewset/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('usersviewset/', user_list, name='user-list'),
    path('usersviewset/<int:pk>/', user_detail, name='user-detail'),
    path('userslist/', views.UserList.as_view(), name='users'),
    path('exampleview/', views.ExampleView.as_view(), name='exmapleview'),
    path('api-token-auth/', DRFView.obtain_auth_token, name='obtainauthtoken'),
    path('api-custom-auth-token/', views.CustomAuthToken.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)
