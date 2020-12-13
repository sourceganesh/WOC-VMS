from django.urls import path,include, reverse_lazy
from django.contrib.auth import views as auth_views
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('register', views.registration_view, name="register"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('authenticate', views.must_authenticate_view, name="must_auth"),
    path('account', views.account_view, name="account"),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='account/password/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='account/password/password_change.html', success_url=reverse_lazy('accounts:password_change_done')), 
        name='password_change'),
]