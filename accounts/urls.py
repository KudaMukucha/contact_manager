from django.urls import path 
from . import views


urlpatterns =[
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('update-profile/',views.update_profile,name='update-profile'),
    path('change-password/',views.change_password,name='change-password'),
    path('account-block',views.account_block,name='account-block'),
    path('register',views.register_user,name='register')
]