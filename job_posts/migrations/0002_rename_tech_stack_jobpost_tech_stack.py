# Generated by Django 4.1 on 2022-08-30 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobpost',
            old_name='Tech_stack',
            new_name='tech_stack',
        ),
    ]