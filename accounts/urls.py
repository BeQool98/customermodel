from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
path('landing_page/', views.landing_page, name = "landing_page"),
    path('register/', views.registerPage, name = "register"),
    path('login/', views.loginPage, name = "login"),
    path('logout/', views.logoutUser, name = "logout"),
    
    path('', views.home, name = "home"), 
    path('user/', views.userPage, name = "user-page"),
    
    path('account/', views.accountSettings, name = 'account'),
    
    path('products/', views.products, name = "products"), 
    path('customer/<str:pk_test>', views.customer, name = "customer"), 
    path('customer_view/<str:pk>', views.customerView, name = "customer_view"), 
    
    
    path("order_processing/", views.orderProcessing, name = "create_order"), 
    path("create_order/", views.createOrder, name = "create_order"), 
    path("update_order/<str:pk>/", views.updateOrder, name = "update_order"),
    path("delete_order/<str:pk>/", views.deleteOrder, name = "delete_order"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "accounts/password_reset.html"),
         name = "reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "accounts/password_reset_sent.html"), 
         name = "password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name = "password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'accounts/password_reset_done.html'),
         name = "password_reset_complete"),
]

