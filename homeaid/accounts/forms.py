from django import forms
from .models import Users,UserProfile
class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        # self.fields['st_username'].widget = forms.TextInput(attrs={
        #     'id': 'username',
        #     'class': 'form-control',
        #     # 'name': 'myCustomName',
        #     'placeholder': 'Username'})
        for field in self.fields:
            self.fields[field].widget = forms.TextInput(attrs={
                'class': 'form-control'})

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=20,label="Email")
    password = forms.CharField(max_length=15,label="Password")

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('image','cover','fname','lname','gender','status')

    fname= forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter First',
            }
        )
    )
    lname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter First',
            }
        )
    )
    selectfields=(('', '--select Gender--'),('male', 'Male'),('female', 'Female'),)
    gender =forms.ChoiceField(choices=selectfields,
                              widget=forms.Select
                              (
                                  attrs={
                                      'class': 'form-control',
                                  }
                              )
                              )







class ChangePasswordForm(forms.Form):
    old =forms.CharField(max_length=100)
    new = forms.CharField(max_length=100)
    repeat = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        self.fields['old'].widget.attrs['class'] = 'form-control'
        self.fields['old'].widget.attrs['placeholder'] = 'Old Password'
        self.fields['new'].widget.attrs['class'] = 'form-control'
        self.fields['new'].widget.attrs['placeholder'] = 'New Password'
        self.fields['repeat'].widget.attrs['class'] = 'form-control'
        self.fields['repeat'].widget.attrs['placeholder'] = 'Reapeat Password'





class ResetPasswordForm(forms.Form):

    email = forms.EmailField(
        label='Enter Your Email :',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Email link with Project ',
            }
        )
    )


class NewPasswordForm(forms.Form):

    new = forms.CharField(max_length=100)
    repeat = forms.CharField(max_length=100)
    new.widget.attrs['class'] = 'form-control'
    repeat.widget.attrs['class'] = 'form-control'

