from django.urls import path
from . import views

app_name = 'inventory_register'

urlpatterns = [
    path('create', views.InventoryCreateView.as_view(), name='create'),
    # path('create_success', views.InventoryCreateSuccessView.as_view(), name='create_success'),
    path('<int:pk>/delete', views.InventoryDeleteView.as_view(), name='delete'),
    path('<int:pk>/detail', views.InventoryDetailView.as_view(), name='detail'),
    path('<int:pk>/', views.InventoryUpdateView.as_view(), name='update'),
    # path('', ),
]