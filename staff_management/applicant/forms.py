from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from applicant.models import ApplicantUser,District,School

import datetime


class ApplicantUserUpdateForm(forms.ModelForm):


    # email = forms.EmailField(
    #     required=True,
    #     # choices=ApplicantUser.CHRONIC_CHOICES,
    #     widget=forms.Select(
    #         attrs={
    #             "class": "form-control formControl",
    #             "id": "email",
    #             'readonly':'readonly'
    #         }
    #     )
    # )
 
    dob = forms.DateField(
    widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
    ),
    )
    join_date = forms.DateField(
    widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
    ),
    )
    
    class Meta:
        model = ApplicantUser
        exclude=('age','experience','au_points','is_eligible')
        read_only=('email',)

    # first_name = forms.CharField(
    #     required=True,
    #     max_length=30,
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control formControl",
    #             "id": "first_name",
    #             "placeholder": "Enter First Name"
    #         }
    #     )
    # )
    # mobile = forms.CharField(
    #     required=False,
    #     max_length=30,
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control formControl",
    #             "id": "mobile",
    #             "placeholder": "Mobile Number"
    #         }

    #     )
    # )
    # aadhaar = forms.CharField(
    #     required=False,
    #     max_length=30,
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control formControl",
    #             "id": "aadhaar",
    #             "placeholder": "Aadhaar"
    #         }

    #     )
    # )


    # child_disease = forms.ChoiceField(
    #     required=True,
    #     choices=ApplicantUser.CHILD_DIS_CHOICES,
    #     widget=forms.Select(
    #         attrs={
    #             "class": "form-control formControl",
    #             "id": "child_disease"
    #         }
    #     )
    # )
 
    # disabled = forms.ChoiceField(
    #     required=True,
    #     choices=ApplicantUser.DIS_CHOICES,
    #     widget=forms.Select(
    #         attrs={
    #             "class": "form-control formControl",
    #             "id": "disabled"
    #         }
    #     )
    # )



    # gender = forms.ChoiceField(
    #     required=True,
    #     choices=ApplicantUser.GENDER_CHOICES,
    #     widget=forms.Select(
    #         attrs={
    #             "class": "form-control formControl",
    #             "id": "gender"
    #         }
    #     )
    # )
    # marial_status = forms.ChoiceField(
    #     required=True,
    #     choices=ApplicantUser.MARITAL_CHOICES,
    #     widget=forms.Select(
    #         attrs={
    #             "class": "form-control formControl",
    #             "id": "marital_status"
    #         }
    #     )
    # )

    # district = forms.ModelChoiceField(
    #     required=True,
    #     queryset=District.objects.all(),
    #     widget=forms.Select(
    #         attrs={
    #             "class": "form-control formControl standardSelect",
    #             "data-live-search": "true",
    #             "data-placeholder": "Select District"
    #         }
    #     )

    # )
    # school = forms.ModelChoiceField(
    #     required=True,
    #     queryset=School.objects.all(),
    #     widget=forms.Select(
    #         attrs={
    #             "class": "form-control formControl standardSelect",
    #             "data-live-search": "true",
    #             "data-placeholder": "Select State"
    #         }
    #     )

    # )
    # def clean_password(self):
    #     # Regardless of what the user provides, return the initial value.
    #     # This is done here, rather than on the field, because the
    #     # field does not have access to the initial value
    #     return self.initial["password"]



# class UserUpdateForm(forms.ModelForm):
#     first_name = forms.CharField(
#         required=True,
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control formControl",
#                 "id": "first_name",
#                 "placeholder": "Enter First Name"
#             }
#         )
#     )
#     last_name = forms.CharField(
#         required=True,
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control formControl",
#                 "id": "last_name",
#                 "placeholder": "Enter Last Name"
#             }
#         )
#     )
#     email = forms.CharField(
#         required=True,
#         max_length=300,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control formControl",
#                 "id": "email",
#                 "placeholder": "Enter Email",
#             }
#         )
#     )
#     password = forms.CharField(
#         required=False,
#         max_length=30,
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control formControl",
#                 "id": "password",
#                 "placeholder": "Enter Password"
#             }

#         ),
#         help_text=("Raw passwords are not stored, so there is no way to see this user's password,"
#                    " but you can change the password")
#     )
#     mobile = forms.CharField(
#         required=True,
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control formControl",
#                 "id": "mobile",
#                 "placeholder": "Enter Mobile"
#             }
#         )
#     )

#     role = forms.ChoiceField(
#         required=True,
#         choices=Us_User.ROLE_CHOICES,
#         widget=forms.Select(
#             attrs={
#                 "class": "form-control formControl",
#             }
#         )
#     )

#     run_time_licenses = forms.ModelMultipleChoiceField(
#         required=False,
#         queryset=RunTimeLicense.objects.all(),
#         widget=forms.SelectMultiple(
#             attrs={
#                 "class": "form-control formControl standardSelect",
#                 "data-live-search": "true",
#                 "data-placeholder": "Select Run Time Licenses"
#             }
#         )
#     )


#     class Meta:
#         model = Us_User
#         fields = ['first_name', 'last_name', 'email', 'password', 'mobile', 'role',
#                   'status', 'run_time_licenses']

#     # def __init__(self, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#     #     instance = kwargs.get('instance')
#     #     workshop = instance.workshop

#     #     if workshop:
#     #         # run_time_license_qs = workshop.run_time_licenses.all()
#     #         # self.fields['run_time_licenses'].queryset = run_time_license_qs
#     #         self.fields['report_to'].queryset = Us_User.objects.filter(
#     #             workshop=workshop).order_by('first_name')

#         # user_obj = instance.user
#         # if user_obj:
#         #     if not user_obj.is_superuser:
#         #         oem_obj = user_obj.us_user.oem or user_obj.oem
#         #         self.fields['user_models'].queryset = Model.objects.filter(oem=oem_obj)