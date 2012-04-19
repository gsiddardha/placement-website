from django import forms
from django.contrib.auth.models import User

GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
        )

class RegisterUserForm(forms.Form):
    username = forms.CharField(max_length = 30)
    first_name = forms.CharField(max_length = 30)
    last_name = forms.CharField(max_length = 30)
    gender = forms.ChoiceField(choices = GENDER_CHOICES)
    department = forms.CharField(max_length = 50)
    joinYear = forms.IntegerField(label='Year of Joining')
    stream = forms.CharField(max_length=10)
    email = forms.EmailField()
    mobile_number = forms.CharField(max_length = 15)
    password = forms.CharField(max_length = 30, widget = forms.PasswordInput)
    password_again = forms.CharField(max_length = 30, widget = forms.PasswordInput)
    
    cgpa = forms.FloatField()
    
    def clean_username(self):
#        if not alnum_re.search(self.cleaned_data['username']):
#            raise forms.ValidationError(u'Usernames can only contain letters, numbers and underscores')
        if User.objects.filter(username = self.cleaned_data['username']):
            pass
        else:
            return self.cleaned_data['username']
        raise forms.ValidationError('This username is already taken. Please choose another.')

    def clean_email(self):
        if User.objects.filter(email = self.cleaned_data['email']):
            pass
        else:
            return self.cleaned_data['email']
        raise forms.ValidationError('This email address is already taken. Please choose another.')

    def clean_password(self):
        if self.prefix:
            field_name1 = '%s-password'%self.prefix
            field_name2 = '%s-password_again'%self.prefix
        else:
            field_name1 = 'password'
            field_name2 = 'password_again'
            
        if self.data[field_name1] !=  '' and self.data[field_name1] !=  self.data[field_name2]:
            raise forms.ValidationError ("The entered passwords do not match.")
        else:
            return self.data[field_name1]
        
class StudentLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

