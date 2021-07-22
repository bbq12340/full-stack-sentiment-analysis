from django.contrib import admin

from .models import InputText
# Register your models here.


class InputTextAdmin(admin.ModelAdmin):
    list_display = ('input_text', 'input_time')
    search_fields = ['input_text']


admin.site.register(InputText, InputTextAdmin)
