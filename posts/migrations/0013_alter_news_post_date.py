# Generated by Django 5.0.2 on 2024-03-05 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_alter_news_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]