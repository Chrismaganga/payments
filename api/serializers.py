from api.models import Address, Coupon, Item, Order, OrderItem, Payment, Refund, UserProfile
from rest_framework import serializers

# # from django_countries.fields import CountryField
# from django_countries.widgets import CountrySelectWidget


# PAYMENT_CHOICES = (
#     ('S', 'Stripe'),
#     ('P', 'PayPal')
# )


# class CheckoutSerializer(serializers.ModelSerializer):
#     shipping_address = serializers.CharField(required=False)
#     shipping_address2 = serializers.CharField(required=False)
#     shipping_country = CountryField(blank_label='(select country)').serializerfield(
#         required=False,
#         widget=CountrySelectWidget(attrs={
#             'class': 'custom-select d-block w-100',
#         }))
#     shipping_zip = serializers.CharField(required=False)

#     billing_address = serializers.CharField(required=False)
#     billing_address2 = serializers.CharField(required=False)
#     billing_country = CountryField(blank_label='(select country)').serializerfield(
#         required=False,
#         widget=CountrySelectWidget(attrs={
#             'class': 'custom-select d-block w-100',
#         }))
#     billing_zip = serializers.CharField(required=False)

#     same_billing_address = serializers.BooleanField(required=False)
#     set_default_shipping = serializers.BooleanField(required=False)
#     use_default_shipping = serializers.BooleanField(required=False)
#     set_default_billing = serializers.BooleanField(required=False)
#     use_default_billing = serializers.BooleanField(required=False)

#     payment_option = serializers.ChoiceField(
#         widget=serializers.RadioSelect, choices=PAYMENT_CHOICES)


# class CouponSerializer(serializers.ModelSerializer):
#     code = serializers.CharField(widget=serializers.TextInput(attrs={
#         'class': 'serializer-control',
#         'placeholder': 'Promo code',
#         'aria-label': 'Recipient\'s username',
#         'aria-describedby': 'basic-addon2'
#     }))


# class RefundSerializer(serializers.ModelSerializer):
#     ref_code = serializers.CharField()
#     message = serializers.CharField(widget=serializers.Textarea(attrs={
#         'rows': 4
#     }))
#     email = serializers.EmailField()


# class PaymentSerializer(serializers.ModelSerializer):
#     stripeToken = serializers.CharField(required=False)
#     save = serializers.BooleanField(required=False)
#     use_default = serializers.BooleanField(required=False)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'



class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'



class RefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refund
        fields = '__all__'
