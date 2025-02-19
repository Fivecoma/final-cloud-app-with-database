from django.contrib import admin
# <HINT> Import any new Models here
from .models import Question, Choice, Submission, Course, Lesson, Instructor, Learner

# <HINT> Register QuestionInline and ChoiceInline classes here

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 3

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    inlines = [QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['content', 'mark']
    list_filter = ['mark']
    search_fields = ['content']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['content', 'is_correct']
    list_filter = ['is_correct']
    search_fields = ['content']

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['id']


# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
