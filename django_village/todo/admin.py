from django.contrib import admin
from .models import Todo
# Register your models here.

class TodoAdmin(admin.ModelAdmin):

	list_display = ['todo', 'is_complete', 'date_published']
	fields       = ['todo', 'is_complete']
	
admin.site.register(Todo, TodoAdmin)