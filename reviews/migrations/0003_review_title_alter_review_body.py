# Generated by Django 4.2 on 2023-07-21 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_alter_review_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.CharField(default='review', max_length=64),
        ),
        migrations.AlterField(
            model_name='review',
            name='body',
            field=models.TextField(default='review'),
        ),
    ]
