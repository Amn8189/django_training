from django.contrib import admin
# Import students model
from .models import Students

# Register your models here.
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'email', 'phonenumber', 'address')

admin.site.register(Students, StudentsAdmin)
