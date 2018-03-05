from django.contrib import admin
from .models import Question
# Register your mfrom .models import Question
from django.contrib import admin

from .models import Question, Choices

class ChoiceInline(admin.TabularInline):
    model = Choices
    extra = 3
   # fields = ['choice_text']
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date', 'choices__votes']
    search_fields = ['question_text']
    date_hierarchy = 'pub_date'
admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choices)