# Generated by Django 4.1.7 on 2023-08-24 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ARVappApi', '0007_zpt_trained_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zpt_trained_model',
            old_name='user_id',
            new_name='project_id',
        ),
    ]
