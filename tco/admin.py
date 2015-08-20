from django.contrib import admin

from .models import Questions
# Register your models here.
class QuestionsAdmin(admin.ModelAdmin):
	class Meta:
		model = Questions

admin.site.register(Questions, QuestionsAdmin)