# Generated by Django 4.1 on 2022-08-30 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_posts', '0002_rename_tech_stack_jobpost_tech_stack'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobpost',
            old_name='company_id',
            new_name='company',
        ),
    ]
