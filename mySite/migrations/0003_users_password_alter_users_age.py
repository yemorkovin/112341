# Generated by Django 4.2 on 2023-04-27 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mySite', '0002_menuitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(default='12345', max_length=70, verbose_name='Password: '),
        ),
        migrations.AlterField(
            model_name='users',
            name='age',
            field=models.IntegerField(verbose_name='Возраст: '),
        ),
    ]
