from django.urls import path

from movies.viewsets.viewset import *

app_name = 'movies'
urlpatterns = [
    # ex: /movies/
    path('', ListAPIView.as_view(), name='list'),
    # ex: /movies/create/
    path('create/', CreateAPIView.as_view(), name='create'),
    # ex: /movies/2/
    path('<int:pk>/', RetrieveAPIView.as_view(), name='detail'),
    # ex: /movies/update/5/
    path('update/<int:pk>/', UpdateAPIView.as_view(), name='update'),
    # ex: /movies/delete/5/
    path('delete/<int:pk>/', DestroyAPIView.as_view(), name='delete')
]