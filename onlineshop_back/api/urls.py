from django.urls import path
from api import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('auth/login/', obtain_jwt_token),
    path('auth/register/', views.register_page, name="register"),
    path('auth/login2/', views.login_page, name="login"),
    path('auth/logout/', views.logout_user, name="logout"),
    path('books/', views.books_list),
    path('journals/', views.journals_list),
]
