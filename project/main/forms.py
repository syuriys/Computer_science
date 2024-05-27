from django import forms
from .models import *


class AboutProgramForm(forms.ModelForm):
    class Meta:
        model = AboutProgram
        fields = '__all__'
        labels = {
            'main_img': 'Головне зображення',
        }


class GeneralInfoForm(forms.ModelForm):
    class Meta:
        model = GeneralInfo
        fields = '__all__'
        labels = {
            'title': 'Заголовок',
            'text': 'Текст'
        }


class SpecialtyFeatureForm(forms.ModelForm):
    class Meta:
        model = SpecialtyFeature
        fields = '__all__'
        labels = {
            'title': 'Заголовок',
            'text': 'Текст'
        }


class CourseOptionForm(forms.ModelForm):
    class Meta:
        model = CourseOption
        fields = '__all__'
        labels = {
            'name': 'Назва курсу',
            'page_link': 'Посилання'
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        labels = {
            'semester': 'Семестр',
            'block': 'Предметний блок',
            'credits': 'Кредити',
            'page_link': 'Посилання'
        }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        labels = {
            'name': "Ім'я",
            'surname': 'Прізвище',
            'position': 'Посада',
            'additional': 'Додатково',
            'image': 'Зображення',
            'page_link': 'Посилання',
        }


class NewsImageForm(forms.ModelForm):
    class Meta:
        model = NewsImage
        fields = '__all__'
        labels = {
            'image': 'Зображення',
        }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        labels = {
            'title': 'Заголовок',
            'content': 'Зміст',
            'publication_date': 'Дата'
        }


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'
        labels = {
            'phone_number': 'Номер телефону',
            'address': 'Адреса',
        }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        labels = {
            'name': "Ім'я",
            'surname': 'Прізвище',
            'message': 'Повідомлення',
            'phone_number': 'Номер телефону'
        }
