from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('user_details/', views.user_details, name='user_details'),
    path('logout/', views.logout_user, name='logout'),
    path('contacts/', views.cont, name='cont'),
    path('', views.dashboard, name='dashboard'),
    path('artwork/<int:artwork_id>/', views.artwork_details, name='artwork_details'),
    path('artwork/<int:artwork_id>/place_order/', views.place_order, name='place_order'),
    path('order_placed/', views.order_placed, name='order_placed'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('static-root/', views.static_root_view, name='static_root'),
]