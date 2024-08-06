from django.urls import path
from . import views

urlpatterns  =[
    path('home/',views.dashboard,name='dashboard'),
    path('create-contact/',views.create_contact,name='create-contact'),
    path('all-contacts/',views.all_contacts,name='all-contacts'),
    path('contact/<int:pk>/',views.edit_contact,name='contact'),
    path('move-to-trash/<int:pk>/',views.move_to_trash,name='move-to-trash'),
    path('trash',views.contacts_trash,name='trash'),
    path('restore-contact/<int:pk>/',views.restore_contact,name='restore-contact'),
    path('delete-contact/<int:pk>/',views.delete_contact,name='delete-contact')
]