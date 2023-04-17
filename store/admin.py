from django.contrib import admin

# Register your models here.
from store.models import Course,Department
admin.site.register(Course)
admin.site.register(Department)
