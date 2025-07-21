from django.urls import path
from tech.views import index, member

urlpatterns = [
    path('', index, name='index'),
    path('members', member, name='member')
]
