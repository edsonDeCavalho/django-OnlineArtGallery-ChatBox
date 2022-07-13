from django.urls import path
from .import views
app_name ='appl'
urlpatterns = [
    path('',views.index,name='index'),
    path('create_Form/', views.create_Form, name='create_Form'),
    path('read/', views.read, name='read'),
    path('update/<id>', views.update, name='update'),
    path('<id>', views.detail,name='detail'),
    path('delate/<id>', views.delete,name="delate")
]