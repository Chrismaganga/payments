from .models import Item, OrderItem, Order, Address, Payment, Coupon, Refund, UserProfile
from rest_framework import mixins, views
from rest_framework.settings import api_settings
from rest_framework.generics import GenericAPIView
from api.models import Item, UserProfile
from api.serializers import ItemSerializer, OrderItemSerializer, UserProfileSerializer
from django.shortcuts import render
from rest_framework.response import Response


def home(request):
    context = {}
    template = 'home.html'
    return render(request, template, context)

class UserProfileCreateModelMixin(mixins.CreateModelMixin,
                    GenericAPIView):  
    queryset = UserProfile.objects.all()               
    serializer_class = UserProfileSerializer                
    """
    Concrete view for creating a model instance.
    """
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserProfileListAPIView(mixins.ListModelMixin,
                  GenericAPIView):
    queryset = UserProfile.objects.all()               
    serializer_class = UserProfileSerializer              
    """
    Concrete view for listing a queryset.
    """
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



class UserProfileRetrieveAPIView(mixins.RetrieveModelMixin,
                      GenericAPIView):
    queryset = UserProfile.objects.all()               
    serializer_class = UserProfileSerializer 
    """
    Concrete view for retrieving a model instance.
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class UserProfileDestroyAPIView(mixins.DestroyModelMixin,
                     GenericAPIView):
    queryset = UserProfile.objects.all()               
    serializer_class = UserProfileSerializer                  
    """
    Concrete view for deleting a model instance.
    """
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UserProfileUpdateAPIView(mixins.UpdateModelMixin,
                    GenericAPIView):
    queryset = UserProfile.objects.all()               
    serializer_class = UserProfileSerializer 
    """
    Concrete view for updating a model instance.
    """
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class UserProfileListCreateAPIView(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        GenericAPIView):
    queryset = UserProfile.objects.all()               
    serializer_class = UserProfileSerializer                 
    """
    Concrete view for listing a queryset or creating a model instance.
    """
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserProfileRetrieveUpdateAPIView(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            GenericAPIView):
    queryset = UserProfile.objects.all()               
    serializer_class = UserProfileSerializer                         
    """
    Concrete view for retrieving, updating a model instance.
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class UserProfileRetrieveDestroyAPIView(mixins.RetrieveModelMixin,
                             mixins.DestroyModelMixin,
                             GenericAPIView):
    queryset = UserProfile.objects.all()               
    serializer_class = UserProfileSerializer                          
    """
    Concrete view for retrieving or deleting a model instance.
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UserProfileRetrieveUpdateDestroyAPIView(mixins.RetrieveModelMixin,
                                   mixins.UpdateModelMixin,
                                   mixins.DestroyModelMixin,
                                   GenericAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer                           
    """
    Concrete view for retrieving, updating or deleting a model instance.
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ItemCreateModelMixin(mixins.CreateModelMixin,
                    GenericAPIView):  
    queryset = Item.objects.all()               
    serializer_class = ItemSerializer                
    """
    Concrete view for creating a model instance.
    """
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ItemListAPIView(mixins.ListModelMixin,
                  GenericAPIView):
    queryset = Item.objects.all()               
    serializer_class = ItemSerializer              
    """
    Concrete view for listing a queryset.
    """
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ItemRetrieveAPIView(mixins.RetrieveModelMixin,
                      GenericAPIView):
    queryset = Item.objects.all()               
    serializer_class = ItemSerializer 
    """
    Concrete view for retrieving a model instance.
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ItemDestroyAPIView(mixins.DestroyModelMixin,
                     GenericAPIView):
    queryset =Item.objects.all()               
    serializer_class = ItemSerializer                  
    """
    Concrete view for deleting a model instance.
    """
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ItemUpdateAPIView(mixins.UpdateModelMixin,
                    GenericAPIView):
    queryset = UserProfile.objects.all()               
    serializer_class = UserProfileSerializer 
    """
    Concrete view for updating a model instance.
    """
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ItemListCreateAPIView(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        GenericAPIView):
    queryset = Item.objects.all()               
    serializer_class = ItemSerializer                
    """
    Concrete view for listing a queryset or creating a model instance.
    """
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ItemRetrieveUpdateAPIView(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            GenericAPIView):
    queryset = Item.objects.all()               
    serializer_class = ItemSerializer                        
    """
    Concrete view for retrieving, updating a model instance.
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ItemRetrieveDestroyAPIView(mixins.RetrieveModelMixin,
                             mixins.DestroyModelMixin,
                             GenericAPIView):
    queryset = Item.objects.all()               
    serializer_class = ItemSerializer                         
    """
    Concrete view for retrieving or deleting a model instance.
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ItemRetrieveUpdateDestroyAPIView(mixins.RetrieveModelMixin,
                                   mixins.UpdateModelMixin,
                                   mixins.DestroyModelMixin,
                                   GenericAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer                          
    """
    Concrete view for retrieving, updating or deleting a model instance.
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class OrderItemCreateModelMixin(mixins.CreateModelMixin,
                    GenericAPIView):  
    queryset =  OrderItem.objects.all()               
    serializer_class = OrderItemSerializer                
    """
    Concrete view for creating a model instance.
    """
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OrderItemListAPIView(mixins.ListModelMixin,
                  GenericAPIView):
    queryset = OrderItem.objects.all()               
    serializer_class = OrderItemSerializer              
    """
    Concrete view for listing a queryset.
    """
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserProfileListAPIView(mixins.ListModelMixin,
                  GenericAPIView):
    queryset = UserProfile.objects.all()               
    serializer_class = UserProfileSerializer              
    """
    Concrete view for listing a queryset.
    """
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



class UserProfileRetrieveAPIView(mixins.RetrieveModelMixin,
                      GenericAPIView):
    queryset = UserProfile.objects.all()               
    serializer_class = UserProfileSerializer 
    """
    Concrete view for retrieving a model instance.
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

