# Generated by Django 4.2 on 2023-05-06 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mySite', '0003_users_password_alter_users_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название категории')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок статьи')),
                ('text', models.TextField(verbose_name='Текст статьи')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mySite.categories')),
            ],
        ),
    ]