# Generated by Django 4.1 on 2022-11-06 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainingapps', '0006_rate_module_that_processed_rate_nbu_sell_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responselog',
            name='path',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='responselog',
            name='query_params',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
