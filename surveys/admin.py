from django.contrib import admin
from .models import Survey, Question

admin.site.register(Survey)


class SurveyAdmin(admin.ModelAdmin):
    readonly_fields = ["date_start"]


admin.site.register(Question)
