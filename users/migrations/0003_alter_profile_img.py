# Generated by Django 4.0.4 on 2022-05-04 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='secret_user_icon', upload_to='user_images', verbose_name='Фото пользователя'),
        ),
    ]
