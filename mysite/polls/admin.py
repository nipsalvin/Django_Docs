from django.contrib import admin
#import Question model
from .models import Question, Choice

# Register your models here.

admin.site.register(Question)
