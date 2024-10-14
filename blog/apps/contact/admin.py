from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'subject', 'date')  # nombre_apellido, asunto, fecha

admin.site.register(Contact, ContactoAdmin)
