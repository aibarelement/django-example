from django.urls import path, include


urlpatterns = [
    path('', include('blogs.urls.v1')),
    path('', include('accounts.urls.v1')),
]
