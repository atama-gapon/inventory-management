from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib import messages

from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse_lazy



urlpatterns = [
    path('admin/', admin.site.urls),

    # トップページはログイン画面
    path('', include('account.urls')),
    path('home/', include('inventory_browse.urls')),
    path('inventory/', include('inventory_register.urls')),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html', from_email='example@example.com'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_mail_done.html'), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirmation.html', post_reset_login=True), name='password_reset_confirm'),
    path('password_reset_finish/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_finish.html'), name='password_reset_complete'),
]

# プロジェクトフォルダのurls.pyにこれを追加しないと、画像は表示されない
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)