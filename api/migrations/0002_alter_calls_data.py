# Generated by Django 5.0.1 on 2024-05-09 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calls',
            name='data',
            field=models.JSONField(default=dict),
        ),
    ]
