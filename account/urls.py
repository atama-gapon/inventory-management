from django.urls import path
from . import views


# urlsからテンプレートを指定する機能
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = 'account'

# login、logoutは「auth_views」を使わないといけない

urlpatterns = [
    # ログインとログアウトは「引数でテンプレートを指定」

    # 参考リンク
    # https://en-junior.com/django-login/#index_id2
    # https://www.cfxlog.com/django_login_logout/#auth_default
    # https://www.cfxlog.com/django-logoutbutton/#rtoc-1
    path('', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('account:login')), name='logout'),

    path('register/', views.RegisterView.as_view(), name='register'),
    path('register_success/', views.RegisterSuccessView.as_view(), name='register_success'),

    # path('', ),
]
