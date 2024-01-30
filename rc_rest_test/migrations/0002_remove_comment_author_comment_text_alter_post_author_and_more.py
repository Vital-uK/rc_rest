# Generated by Django 5.0.1 on 2024-01-30 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rc_rest_test', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
