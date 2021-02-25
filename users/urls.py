from django.urls import path

from users.viewsets.viewset import *

app_name = 'users'
urlpatterns = [
    # ex: /users/
    path('', ListAPIView.as_view(), name='list'),
    # ex: /users/create/
    path('create/', CreateAPIView.as_view(), name='create'),
    # ex: /users/2/
    path('<int:pk>/', RetrieveAPIView.as_view(), name='detail'),
    # ex: /users/update/5/
    path('update/<int:pk>/', UpdateAPIView.as_view(), name='update'),
    # ex: /users/delete/5/
    path('delete/<int:pk>/', DestroyAPIView.as_view(), name='delete'),
    # ex: /users/logout
    path('logout/', Logout.as_view()),
]