from django.urls import path
from . import views

urlpatterns = [
    path('', views.youtubers, name="youtubers"),
    path('search', views.search, name="search"),
    path('<int:id>', views.youtubers_detail, name="youtubers_detail"),
                    
]                   