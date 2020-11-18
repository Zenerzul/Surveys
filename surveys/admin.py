from django.contrib import admin
from .models import Survey, Question


class SurveyAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["date_start"]
        else:
            return []


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question)
