from django import forms
from django.db import models
from .models import *

class StaffForm(forms.ModelForm):
    sid = forms.CharField(widget=
        forms.TextInput(attrs={'class':'form-control input-box-reg', 'maxlength':'8', }),
    )
    username = forms.CharField(widget=
        forms.TextInput(attrs={'class':'form-control input-box-reg'}),
    )
    password1 = forms.CharField(widget=
        forms.TextInput(attrs={'class':'form-control input-box-reg', 'type':'password'}),
        label="Password"
    )
    password2 = forms.CharField(widget=
        forms.TextInput(attrs={'class':'form-control input-box-reg', 'type':'password'}),
        label="Password Confirm"
    )

    first_name = forms.CharField(widget=
        forms.TextInput(attrs={'class':'form-control input-box-reg'}),
    )
    last_name = forms.CharField(widget=
        forms.TextInput(attrs={'class':'form-control input-box-reg'}),
    )

    CHOICES = (('M', 'ชาย'),('F', 'หญิง'),)
    sex = forms.ChoiceField(choices=CHOICES, widget=
        forms.Select(attrs={'class':'form-control select'}))

    birthday = forms.ChoiceField(widget=
        forms.TextInput(attrs={'class':'form-control input-box-reg date', 'type':'date'}),
    )

    CHOICES = (('A', 'A'),('B', 'B'),('AB', 'AB'),('O', 'O'))
    blood_type = forms.ChoiceField(choices=CHOICES, widget=
        forms.Select(attrs={'class':'form-control select'}))

    CHOICES = (('buddha', 'พุทธ'),('christ', 'คริสต์'),('islamic', 'อิสลาม'),('other', 'อื่นๆ/ไม่ระบุ'))
    religion = forms.ChoiceField(choices=CHOICES, widget=
        forms.Select(attrs={'class':'form-control select'}))
    
    CHOICES = (('S', 'S'),('M', 'M'),('L', 'L'),('XL', 'XL'),('XXL', 'XXL'))
    shirt_size = forms.ChoiceField(choices=CHOICES, widget=
        forms.Select(attrs={'class':'form-control select'}))
    
    # is_accept = forms.BooleanField()
    phone = forms.CharField(widget=
        forms.TextInput(attrs={'class':'form-control input-box-reg'}),
    )
    email = forms.EmailField(widget=
        forms.TextInput(attrs={'class':'form-control input-box-reg'}),
    )

    food_allergy = forms.CharField(widget=
        forms.TextInput(attrs={'class':'form-control input-box-reg'}),
    )

    congenital_disease = forms.CharField(widget=
        forms.TextInput(attrs={'class':'form-control input-box-reg'}),
    )

    position = forms.CharField(widget=
        forms.TextInput(attrs={'class':'form-control input-box-reg'}),
    )

    group = forms.CharField(widget=
        forms.TextInput(attrs={'class':'form-control input-box-reg'}),
    )

    profile_pic = forms.ImageField(required=True, widget=
        forms.FileInput(attrs={'class':'custom-file-input', 'aria-describedby':'inputGroupFileAddon01'})
    )

    class Meta:
        model = Staff
        fields = (
            'position',
            'department',
            'mc',
            'group'
        )

    