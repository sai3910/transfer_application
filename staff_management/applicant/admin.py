from django.contrib import admin
from .models import ApplicantUser,District,School
# Register your models here.
admin.site.register(ApplicantUser)
admin.site.register(District)
admin.site.register(School)
