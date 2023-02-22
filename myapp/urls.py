from django.urls import path
from .views import *

urlpatterns=[
    # path('url name/',function_name)
    path('intex/',intex),
    path('login/',login),
    path('register/',register),
    path('shoplogin/',shoplogin),
    path('shopregister/',shopregister),
    path('display/',display),
    path('sellerprofile/',sellerprofile),
    path('sellerdisplay/',sellerdisplay),
    path('userprofile/',userprofile),
    path('fileupload/',fileupload),
    path('filedisplay/',filedisplay),
    path('filedelete/<int:id>',filedelete),   #<int:id>-->given because data is deleted by using id.
    path('fileedit/<int:id>',fileedit),
    path('registeration/',registeration),
    path('userlogin/',userlogin),
    path('verify/<auth_token>',verify), #string
    path('filedisplayuser/',filedisplayuser),
    path('addtocart/<int:id>',addtocart),
    path('addcartwishlist/<int:id>',addcartwishlist),
    path('cartdisplay/',cartdisplay),
    path('addtowishlist/<int:id>',addtowishlist),
    path('wishlistdisplay/',wishlistdisplay),
    path('removecart/<int:id>',removecart),
    path('removewishlist/<int:id>',removewishlist),
    path('cartbuy/<int:id>',cartbuy),
    path('cardpayment/',cardpayment),
    path('orderstatus/',orderstatus)
]
