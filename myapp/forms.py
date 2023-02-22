from django import forms

# class regform(forms.Form):
#     name=forms.CharField(max_length=30)
#     email=forms.EmailField()
#     phone=forms.IntegerField()
#     address=forms.CharField(max_length=100)
#     pincode=forms.IntegerField()
#     password=forms.CharField(max_length=20)
#     confirm_password=forms.CharField(max_length=20)

class regform(forms.Form):
    username=forms.CharField(max_length=30)
    first_name=forms.CharField(max_length=30)
    last_name= forms.CharField(max_length=30)
    email=forms.EmailField()
    password=forms.CharField(max_length=20)
    confirm_password=forms.CharField(max_length=20)

# class logform(forms.Form):
#     name=forms.CharField(max_length=30)
#     email=forms.EmailField()
#     password=forms.CharField(max_length=30)

class logform(forms.Form):
    username=forms.CharField(max_length=30)
    email=forms.EmailField()
    password=forms.CharField(max_length=30)


class regsellerform(forms.Form):
    sname=forms.CharField(max_length=30)
    address=forms.CharField(max_length=100)
    email=forms.EmailField()
    phone=forms.IntegerField()
    pincode=forms.IntegerField()
    password=forms.CharField(max_length=20)
    confirm_password=forms.CharField(max_length=20)

class logsellerform(forms.Form):
    sname=forms.CharField(max_length=30)
    email=forms.EmailField()
    password=forms.CharField(max_length=30)

class fileform(forms.Form):
    pname=forms.CharField(max_length=40)
    pprize=forms.IntegerField()
    pdes=forms.CharField(max_length=100)
    pimage=forms.ImageField()

class customercardpay(forms.Form):
    cardname=forms.CharField(max_length=30)
    cardnumber=forms.CharField(max_length=30)
    cardexpiry=forms.CharField(max_length=30)
    securitycode=forms.CharField(max_length=30)