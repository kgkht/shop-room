from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('settings/<int:pk>/update', views.SiteSettingsUpdateView.as_view(), name='site-settings'),
    path('users/', views.UserListView.as_view(), name='all-users'),
    path('user/account/create/', views.UserAccountCreateView.as_view(), name='account_create'),
    path('myaccount/<int:pk>/update/', views.UserAccountUpdateView.as_view(), name='account_update'),

    
    path('user/profile/<int:pk>/update/', views.UserProfileUpdateView.as_view(), name='profile_update'),
    path('user/profile/create', views.UserProfileCreateView.as_view(), name='profile_create'),
    path('user/<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),
#    path('change-password/', auth_views.PasswordChangeView.as_view()),

    
    path('products/', views.ProductsListView.as_view(), name='all-products'),
    path('product/detail/<uuid:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('product/item/create', views.ProductCreateView.as_view(), name='product_item_create'),
    path('product/price/create', views.PriceCreateView.as_view(), name='product_price_create'),
    path('product/stock/create', views.StockCreateView.as_view(), name='product_stock_create'),
    path('product/images/create', views.ProductImagesCreateView.as_view(), name='product_images_create'),
    
]
