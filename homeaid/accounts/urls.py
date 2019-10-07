from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^register/$', views.user_register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    # url(r'^otp/$', views.otp, name='otp'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^userprofile/$', views.user_profile, name='userprofile'),
    url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),
    url(r'^user_changepassword/$', views.user_changepassword, name='user_changepassword'),
    url(r'^user_resetpassword/$', views.user_resetpassword, name='user_resetpassword'),
    url(r'^user_logout/$', views.user_logout, name='user_logout'),


]