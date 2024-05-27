from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from tinymce.models import HTMLField

# Create your models here.


class AboutProgram(models.Model):
    main_img = models.ImageField(upload_to='main_images/')

    def __str__(self):
        return "Про програму"

    class Meta:
        verbose_name = "Про програму"
        verbose_name_plural = "Про програму"


class GeneralInfo(models.Model):
    about_program = models.ForeignKey(
        AboutProgram, related_name='general_info', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Загальна інформація"
        verbose_name_plural = "Загальна інформація"


class SpecialtyFeature(models.Model):
    about_program = models.ForeignKey(
        AboutProgram, related_name='features', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Особливість спеціальності"
        verbose_name_plural = "Особливості спеціальності"


class Course(models.Model):
    SEMESTER_CHOICES = [(i, f"Семестр {i}") for i in range(1, 9)]
    BLOCK_CHOICES = [
        ('Гуманітарний блок', 'Гуманітарний блок'),
        ('Природничо-науковий блок', 'Природничо-науковий блок'),
        ('Фаховий блок', 'Фаховий блок'),
        ('Фахові дисципліни вільного вибору', 'Фахові дисципліни вільного вибору'),
    ]

    name = models.CharField(max_length=100, verbose_name="Назва курсу")
    semester = models.IntegerField(
        choices=SEMESTER_CHOICES, verbose_name="Семестр")
    block = models.CharField(
        max_length=100, choices=BLOCK_CHOICES, verbose_name="Предметний блок")
    credits = models.IntegerField(
        verbose_name="Кредити",
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )
    page_link = models.URLField()

    def __str__(self):
        options = self.options.all()
        option_names = ' / '.join([option.name for option in options])
        return f"{self.semester} семестр - {self.name} / {option_names}" if options else f"{self.semester} семестр - {self.name}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курси"
        ordering = ['-semester']


class CourseOption(models.Model):
    course = models.ForeignKey(
        Course, related_name='options', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Назва курсу")
    page_link = models.URLField(verbose_name="Посилання на курс")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Додаткова опція"
        verbose_name_plural = "Додаткові опції"


class News(models.Model):
    title = models.CharField(max_length=255)
    content = HTMLField()
    publication_date = models.DateField()

    def __str__(self):
        return f"{self.title} - {self.publication_date.strftime('%d.%m.%Y')}"

    class Meta:
        verbose_name = "Новина"
        verbose_name_plural = "Новини"
        ordering = ['-publication_date']


class NewsImage(models.Model):
    news = models.ForeignKey(
        News, related_name='images', on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='news_images/')

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = "Зображення новини"
        verbose_name_plural = "Зображення новин"


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    additional = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='teachers_images/')
    page_link = models.URLField()

    def __str__(self):
        return f'{self.surname} {self.name}'

    class Meta:
        verbose_name = "Викладач"
        verbose_name_plural = "Викладачі"
        ordering = ['surname']


class Feedback(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"


class Contacts(models.Model):
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    instagram = models.URLField()
    facebook = models.URLField()

    def __str__(self):
        return "Контакти"

    class Meta:
        verbose_name = "Контакти"
        verbose_name_plural = "Контакти"
