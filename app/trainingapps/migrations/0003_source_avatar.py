# Generated by Django 4.1 on 2022-09-12 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainingapps', '0002_rate_source_alter_contactus_email_from'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='avatar',
            field=models.FileField(default='', upload_to='logo'),
            preserve_default=False,
        ),
    ]
