from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("loggedin/", views.register, name="loggedin"),
    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.signout, name="logout"),
    path("reset_password/", views.PasswordReset.as_view(),
        {"template_name":'registration/password _reset_form.html'},
    name='password_reset'),
        path("password_reset_complete/", auth_views.PasswordResetCompleteView.as_view(), {"template_name" : "registration/password_reset_complete.html"},
        name="password_reset_complete"),
    path("password_change/", auth_views.PasswordChangeView.as_view(),
        {"template_name": "registration/password _change_form.html"},
        name="password_change"),
    path("password_reset_done/", auth_views.PasswordResetDoneView.as_view(),
        {"template_name": "registration/password _reset_done_form.html"},
        name='password_reset_done'),
    path("password_change_done/", auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    #path("password_reset_sent/", auth_views.PasswordResetSentView.as_view(), {"template_name": "registration/password _reset_sent.html"},                 name='password_reset_sent'),
    ]

