from django.urls import path, include

urlpatterns = [
    path("core/", include("api.v1.urls")),    
]
