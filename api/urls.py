# from django.urls import path
# from .views import (
#     ItemDetailView,
#     CheckoutView,
#     HomeView,
#     OrderSummaryView,
#     add_to_cart,
#     remove_from_cart,
#     remove_single_item_from_cart,
#     PaymentView,
#     AddCouponView,
#     RequestRefundView
# )

# app_name = 'api'

# urlpatterns = [
#     path('home/', HomeView.as_view(), name='home'),
#     path('checkout/', CheckoutView.as_view(), name='checkout'),
#     path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
#     path('product/<slug>/', ItemDetailView.as_view(), name='product'),
#     path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
#     path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
#     path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
#     path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
#          name='remove-single-item-from-cart'),
#     path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
#     path('request-refund/', RequestRefundView.as_view(), name='request-refund')
# ]

from django.urls import path,include

from api.views import ItemCreateModelMixin, ItemDestroyAPIView, ItemListAPIView, ItemListCreateAPIView, ItemRetrieveAPIView, ItemRetrieveDestroyAPIView, ItemRetrieveUpdateAPIView, ItemRetrieveUpdateDestroyAPIView, ItemUpdateAPIView, UserProfileCreateModelMixin, UserProfileListAPIView, UserProfileListCreateAPIView, UserProfileRetrieveDestroyAPIView, UserProfileRetrieveUpdateAPIView, UserProfileRetrieveUpdateDestroyAPIView



urlpatterns = [
    path('', UserProfileCreateModelMixin.as_view(), name='create'),
    path('lists/<int:pk>/', UserProfileListAPIView.as_view(), name='lists'),
    path('list-create/<int:pk>/', UserProfileListCreateAPIView.as_view(), name='listcreate'),
    path('retrieve-update/<int:pk>/', UserProfileRetrieveUpdateAPIView.as_view(), name='retrieveupdate'),
    path('retrieve-destroy/<int:pk>/', UserProfileRetrieveDestroyAPIView.as_view(), name='retrieveupdate'),
    path('retrieve-update-destroy/<int:pk>/',UserProfileRetrieveUpdateDestroyAPIView.as_view(), name='retrieveupdatedestroy'),
    path('item-create/',ItemCreateModelMixin.as_view( ), name='itemcreate'),
    path('item-retrieve/<int:pk>', ItemRetrieveAPIView.as_view(), name='item-retrieve'),
    path('item-list/<int:pk>', ItemDestroyAPIView.as_view(), name='item-destroy'),
    path('item-list/<int:pk>', ItemUpdateAPIView.as_view(), name='item-update'),
    path('item-list-create/<int:pk>', ItemListCreateAPIView.as_view(), name='item-list-create'),
    path('item-retrieve-update/<int:pk>', ItemRetrieveUpdateAPIView.as_view(), name='item-retrieve-update'),
    path('item-retrieve-destroy/<int:pk>', ItemRetrieveDestroyAPIView.as_view(), name='item-retrieve-destroy'), 
    path('item-retrieve-update-destroy/<int:pk>', ItemRetrieveUpdateDestroyAPIView.as_view(), name='item-retrieve-update-destroy'),

]



    
