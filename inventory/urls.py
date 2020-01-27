from django.contrib import admin
from django.urls import path, include

from inventory.views import list_inven, create_inven, detail_inven, apply_opponent, detail_opponent, list_opponent

urlpatterns = [
    path('', list_inven, name='list_inven'),
    path('create/', create_inven, name='create_inven'),
    path('<int:pk>', detail_inven, name='detail_inven'),
    path('apply/', apply_opponent, name='apply_opponent'),
    path('opponent/<int:pk>/', detail_opponent, name='detail_opponent'),
    path('opponent/list/', list_opponent, name='list_opponent'),
]
