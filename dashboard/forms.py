# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(required=False)  # <-- make sure this is False
#     first_name = forms.CharField(required=True, max_length=30)
#     last_name = forms.CharField(required=True, max_length=30)

#     class Meta:
#         model = User
#         fields = ("username", "first_name", "last_name", "email", "password1", "password2")

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Explicitly mark email as not required (redundant but safe)
#         self.fields['email'].required = False

#         # Add bootstrap classes
#         self.fields['username'].widget.attrs.update({'class': 'form-control'})
#         self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
#         self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
#         self.fields['email'].widget.attrs.update({'class': 'form-control'})
#         self.fields['password1'].widget.attrs.update({'class': 'form-control'})
#         self.fields['password2'].widget.attrs.update({'class': 'form-control'})

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.email = self.cleaned_data.get('email', '')  # use empty string if blank
#         user.is_active = True  # Explicitly set active status to True
#         if commit:
#             user.save()
#         return user




# # forms.py
# from django import forms
# from .models import EmployeeMaster

# class EmployeeMasterForm(forms.ModelForm):
#     class Meta:
#         model = EmployeeMaster
#         fields = ['Employee_name', 'Team_leader', 'Partner', 'Admin']
#         widgets = {
#             'Employee_name': forms.TextInput(attrs={'class': 'input', 'autocomplete': 'on'}),
#             'Team_leader': forms.TextInput(attrs={'class': 'input'}),
#             'Partner': forms.TextInput(attrs={'class': 'input'}),
#             'Admin': forms.TextInput(attrs={'class': 'input'}),
#         }




# from django import forms
# from .models import ClientMaster

# class ClientMasterForm(forms.ModelForm):
#     class Meta:
#         model = ClientMaster
#         fields = ['audit_manager', 'Head', 'Client_name']  # reordered here
#         widgets = {
#             'Client_name': forms.TextInput(attrs={'class': 'input'}),
#             'audit_manager': forms.TextInput(attrs={'class': 'input'}),
#             'Head': forms.TextInput(attrs={'class': 'input'}),
#         }



from django import forms
from django.contrib.auth.models import User
from .models import EmployeeMaster, ClientMaster, Planning

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeMaster
        fields = ['Employee_name', 'audit_manager', 'Partner', 'Admin']

class ClientForm(forms.ModelForm):
    class Meta:
        model = ClientMaster
        fields = ['Client_name', 'audit_manager', 'Partner']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'email']

class PlanningForm(forms.ModelForm):
    class Meta:
        model = Planning
        fields = ['date', 'employee_name', 'client_name', 'fullday_halfday', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }



# forms.py
from django import forms

class HolidayForm(forms.Form):
    from_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    to_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    fullday_halfday = forms.ChoiceField(
        choices=[('Full Day', 'Full Day'), ('Half Day', 'Half Day')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'style': 'height: 60px; max-height: 120px;'})
    )
