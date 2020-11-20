from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *
# use generic views and templates for accounts
urlpatterns = [
    # for login, logout, we directly use generic views
    # login requires template registration/login.html
    path('login/', LoginView.as_view(), name='login'),
    # logout uses default template, set template name for custom template
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', register, name='register'),
]