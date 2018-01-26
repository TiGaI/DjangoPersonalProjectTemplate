from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# admin.TabularInline each box is style together in one box
# admin.StackedInline - each box is style stacked 
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	fieldsets = [
		(None,               {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
	list_filter = ['pub_date']


admin.site.register(Question, QuestionAdmin)