# Generated by Django 4.1.7 on 2023-08-24 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ARVappApi', '0008_rename_user_id_zpt_trained_model_project_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestZPT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='ZPT_File/')),
            ],
        ),
    ]
