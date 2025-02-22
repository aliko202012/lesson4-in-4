# Generated by Django 5.1.2 on 2024-10-14 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_blog_delete_employees'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя сотрудника')),
                ('image', models.ImageField(upload_to='image/', verbose_name='Фото сотрудника')),
                ('position', models.CharField(max_length=255, verbose_name='Должность')),
                ('facebook', models.URLField(verbose_name='Ссылка на facebook')),
                ('twitter', models.URLField(verbose_name='Ссылка на twitter')),
                ('github', models.URLField(verbose_name='Ссылка на Github')),
                ('google', models.URLField(verbose_name='Ссылка на Google +')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.AlterModelOptions(
            name='basesettings',
            options={'verbose_name': 'Основная настройка сайта', 'verbose_name_plural': 'Основные настройки сайта'},
        ),
        migrations.AlterModelOptions(
            name='blog',
            options={},
        ),
        migrations.AlterField(
            model_name='basesettings',
            name='facebook',
            field=models.URLField(verbose_name='Ссылка на facebook'),
        ),
        migrations.AlterField(
            model_name='basesettings',
            name='google',
            field=models.URLField(verbose_name='Ссылка на Google +'),
        ),
    ]
