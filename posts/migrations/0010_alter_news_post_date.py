# Generated by Django 5.0.2 on 2024-03-05 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_alter_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='post_date',
            field=models.DateTimeField(),
        ),
    ]
