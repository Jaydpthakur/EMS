from django.contrib import admin
from .models import UserData,AdminDataBase,EnquiryDataBase
# Register your models here.

admin.site.register(UserData)
admin.site.register(AdminDataBase)
admin.site.register(EnquiryDataBase)