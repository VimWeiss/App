# Generated by Django 5.0.2 on 2024-02-27 01:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iablog', '0003_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=50, verbose_name='IP-адрес')),
                ('pos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iablog.post', verbose_name='Публикация')),
            ],
        ),
    ]
