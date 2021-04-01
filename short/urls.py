from django.urls import path
from .views import Home,Send
urlpatterns = [ 
    path('',Home),
    path('<str:code>',Send)
]