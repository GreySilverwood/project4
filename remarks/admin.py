from django.contrib import admin

#import the Remarks model
from .models import Remark

# Register your models here.
admin.site.register(Remark)