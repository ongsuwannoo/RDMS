from django import forms
from django.contrib.auth.forms import UserCreationForm
from index.models import user
from django.db import models

class regForm(UserCreationForm):
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
    
    # is_accept = forms.BooleanField()
    phone = forms.CharField(widget=
        forms.TextInput(attrs={'class':'form-control input-box-reg'}),
    )
    email = forms.EmailField(widget=
        forms.TextInput(attrs={'class':'form-control input-box-reg'}),
    )
    profile_pic = forms.ImageField(required=True, widget=
        forms.FileInput(attrs={'class':'custom-file-input', 'aria-describedby':'inputGroupFileAddon01'})
    )

    class Meta:
        model = user
        fields = (
            'username',
            'password1',
            'password2',
            'sid',
            'sex',
            'first_name',
            'last_name',
            'profile_pic',
            'phone',
            'email',
            # 'is_accept',
        )

    def save(self, commit=True):
        user = super(regForm, self).save(commit=False)
        user.sid = self.cleaned_data['sid']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.sex = self.cleaned_data['sex']
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        # user.is_accept = self.cleaned_data['is_accept']
        user.profile_pic = self.cleaned_data['profile_pic']

        if commit:
            user.save()
        return user