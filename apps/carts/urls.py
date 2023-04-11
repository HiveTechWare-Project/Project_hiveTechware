from django.urls import path
from . import views 


urlpatterns=[
    path('', views.CartList.as_view(), name='Cart List'),
    path('add/', views.CartAdd.as_view(), name='Cart Add'),
    path('update/<int:id>', views.CartUpdate.as_view(), name='Cart Update'),
]