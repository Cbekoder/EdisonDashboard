# Generated by Django 5.0.1 on 2024-02-24 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphics', '0005_rename_nodegroup_nodegroups'),
    ]

    operations = [
        migrations.AddField(
            model_name='nodegroups',
            name='status',
            field=models.CharField(blank=True, choices=[('New', 'New'), ('Active', 'Active'), ('Inactive', 'Inactive'), ('Archived', 'Archived')], max_length=10),
        ),
    ]
