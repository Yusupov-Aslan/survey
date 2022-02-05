from django.contrib import admin

# Register your models here.

from survey.models import Poll, Choice


class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'created_at']
    list_filter = ['question']
    fields = ['question']
    readonly_fields = ['created_at']


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
