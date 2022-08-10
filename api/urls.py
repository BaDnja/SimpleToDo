from django.urls import path, include

urlpatterns = [
    path('profiles/', include('profiles.urls')),
    path('groups/', include('groups.urls')),
    path('lists/', include('lists.urls')),
]
