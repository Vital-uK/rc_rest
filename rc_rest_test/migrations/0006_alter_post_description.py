# Generated by Django 5.0.1 on 2024-01-30 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rc_rest_test', '0005_alter_comment_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
