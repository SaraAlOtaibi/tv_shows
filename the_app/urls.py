from django.urls import path     
from . import views

urlpatterns = [
    path('', views.shows, name='all_shows'),
    path('new',views.add_show_temp, name='show_creation_page'),
    path('add_show',views.add_show, name='add_show'),
    path('<int:show_id>',views.view, name='view_show'),
    path('<int:show_id>/edit',views.edit, name='edit_show'),
    path('<int:show_id>/destroy',views.delete, name='delete_show'),
    path('<int:show_id>/update_show', views.update, name='update_show' )
]