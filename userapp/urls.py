from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('add',views.add),
    path('view',views.view),
    path('edit',views.edit),
    path('update',views.update),
    path('delete',views.delete),
]