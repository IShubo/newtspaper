from django.contrib import admin
from .models import Articles, Profile


# Register your models here.
admin.site.register(Profile)


admin.site.register(Articles)