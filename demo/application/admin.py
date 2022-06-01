from django.contrib import admin
from .models import (
    Question,
    Choice
)


class ChoiceInline(admin.TabularInline):  # admin.StackedInline
    model = Choice
    extra = 3
    fields = ['choice_text']


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (
            None,
            {
                'fields': ['question_text']
            }
        ),
        (
            'Date information',
            {
                'fields': ['pub_date']
            }
        ),
    ]
    inlines = [
        ChoiceInline
    ]
    list_display = ['question_text', 'pub_date', 'was_published_recently']
    list_filter = ['pub_date']


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
