from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=70, verbose_name="Имя: ")
    age = models.IntegerField(verbose_name="Возраст: ")
    email = models.EmailField(verbose_name="Email: ")
    poll = [
        ('m', 'мужской'),
        ('w', 'женский')
    ]
    poll = models.CharField(choices=poll, max_length=1, verbose_name="Ваш пол: ")
    password = models.CharField(max_length=70, verbose_name='Password: ', default='12345')
    def __str__(self):
        return self.name

class MenuItem(models.Model):
    title = models.CharField(max_length=70,verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="images", verbose_name="Картинка")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    TYPE = [
        ('BRX', 'Завтрак'),
        ('LUN', 'Обед'),
        ('DIC', 'Ужин')
    ]
    type = models.CharField(choices=TYPE, max_length=3, default='BRX', verbose_name='Тип')

    def __str__(self):
        return self.title
# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок статьи')
    text = models.TextField(verbose_name='Текст статьи')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to="images/news", verbose_name='Картинка', default='1.jpg')

    def __str__(self):
        return self.title