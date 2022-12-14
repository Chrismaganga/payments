from django.urls import path,include
from . import views
from api.views import  ItemCreateModelMixin, ItemDestroyAPIView, ItemListAPIView, ItemListCreateAPIView, ItemRetrieveAPIView, ItemRetrieveDestroyAPIView, ItemRetrieveUpdateAPIView, ItemRetrieveUpdateDestroyAPIView, ItemUpdateAPIView, OrderItemCreateModelMixin, UserProfileCreateModelMixin, UserProfileListAPIView, UserProfileListCreateAPIView, UserProfileRetrieveDestroyAPIView, UserProfileRetrieveUpdateAPIView, UserProfileRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('home/', views.home, name='home'),
    path('userprofile-create/', UserProfileCreateModelMixin.as_view(), name='create'),
    path('userprofile-lists/<int:pk>/', UserProfileListAPIView.as_view(), name='lists'),
    path('userprofile-list-create/<int:pk>/', UserProfileListCreateAPIView.as_view(), name='listcreate'),
    path('userprofile-retrieve-update/<int:pk>/', UserProfileRetrieveUpdateAPIView.as_view(), name='retrieveupdate'),
    path('userprofile-retrieve-destroy/<int:pk>/', UserProfileRetrieveDestroyAPIView.as_view(), name='retrieveupdate'),
    path('userprofile-retrieve-update-destroy/<int:pk>/',UserProfileRetrieveUpdateDestroyAPIView.as_view(), name='retrieveupdatedestroy'),
    path('item-create/',ItemCreateModelMixin.as_view( ), name='itemcreate'),
    path('item-retrieve/<int:pk>', ItemRetrieveAPIView.as_view(), name='item-retrieve'),
    path('item-list/<int:pk>', ItemDestroyAPIView.as_view(), name='item-destroy'),
    path('item-list/<int:pk>', ItemUpdateAPIView.as_view(), name='item-update'),
    path('item-list-create/<int:pk>', ItemListCreateAPIView.as_view(), name='item-list-create'),
    path('item-retrieve-update/<int:pk>', ItemRetrieveUpdateAPIView.as_view(), name='item-retrieve-update'),
    path('item-retrieve-destroy/<int:pk>', ItemRetrieveDestroyAPIView.as_view(), name='item-retrieve-destroy'), 
    path('item-retrieve-update-destroy/<int:pk>', ItemRetrieveUpdateDestroyAPIView.as_view(), name='item-retrieve-update-destroy'),
    path('orde-item-create/', OrderItemCreateModelMixin.as_view( ), name='order-item-create'),
    path('order-item-list/<int:pk>', OrderItemCreateModelMixin.as_view( ), name='order-item-list'), 
]



    
