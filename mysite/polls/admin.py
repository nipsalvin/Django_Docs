from django.contrib import admin

# Register your models here.

from .models import Choice, Question

admin.site.register(Question) #include model to be added to the admin panel
admin.site.register(Choice)

