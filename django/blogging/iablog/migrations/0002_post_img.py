# Generated by Django 5.0.2 on 2024-02-22 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iablog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='img.jpg', upload_to='image/%Y', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]