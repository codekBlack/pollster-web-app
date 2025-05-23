from django.contrib import admin

from .models import Question, Choice

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Admin Area"
admin.site.index_title = "Welcome to the Admin Area"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields' : ['question_text']}),
                 ('Date Published', {'fields' : ['pub_date'], 'classes' : ['collapse']}),]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)


