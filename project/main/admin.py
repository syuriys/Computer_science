from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.


class SpecialtyFeatureInline(admin.TabularInline):
    model = SpecialtyFeature
    form = SpecialtyFeatureForm
    extra = 1


class GeneralInfoInline(admin.TabularInline):
    model = GeneralInfo
    form = GeneralInfoForm
    extra = 1


class AboutProgramAdmin(admin.ModelAdmin):
    form = AboutProgramForm
    inlines = [GeneralInfoInline, SpecialtyFeatureInline]


admin.site.register(AboutProgram, AboutProgramAdmin)


class CourseOptionInline(admin.TabularInline):
    model = CourseOption
    form = CourseOptionForm
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    form = CourseForm
    inlines = [CourseOptionInline]


admin.site.register(Course, CourseAdmin)


class NewsImageInline(admin.TabularInline):
    model = NewsImage
    form = NewsImageForm
    extra = 1


class NewsAdmin(admin.ModelAdmin):
    form = NewsForm
    inlines = [NewsImageInline]


admin.site.register(News, NewsAdmin)


class TeacherAdmin(admin.ModelAdmin):
    form = TeacherForm


admin.site.register(Teacher, TeacherAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    form = FeedbackForm


admin.site.register(Feedback, FeedbackAdmin)


class ContactsAdmin(admin.ModelAdmin):
    form = ContactsForm


admin.site.register(Contacts, ContactsAdmin)
