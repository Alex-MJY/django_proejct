# Generated by Django 3.2.15 on 2022-10-23 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cattube', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='view_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]