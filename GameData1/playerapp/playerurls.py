from django.urls import path

from playerapp import views

urlpatterns = [
    path('', views.overall, name='overall'),
    path('viewData/', views.view_data, name='view_data'),
    path('add/', views.add_player, name='adduser'),
    path('editPlayer/<id>', views.edit_player, name='edit_player'),
    path('deletePlayer/<id>', views.delete_player, name='delete_player'),

]