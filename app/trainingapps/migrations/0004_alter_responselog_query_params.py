# Generated by Django 4.1 on 2022-09-16 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainingapps', '0003_source_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responselog',
            name='query_params',
            field=models.CharField(max_length=20, null=True),
        ),
    ]