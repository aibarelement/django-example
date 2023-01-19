from django.urls import path, include


urlpatterns = [
    path('', include('blogs.urls.v2')),
    path('', include('accounts.urls.v2')),
]
