
from django.urls import path
# from .views import article_list
# from .views import article_detail

from . import views
urlpatterns = [

    path('article/', views.article_list),
    path('detail/<int:pk>/', views.article_detail),
    
]
