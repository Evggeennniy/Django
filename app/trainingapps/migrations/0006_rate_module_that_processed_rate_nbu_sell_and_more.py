# Generated by Django 4.1 on 2022-10-02 18:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trainingapps', '0005_contactus_created_rate_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='module_that_processed',
            field=models.CharField(
                choices=[
                    ('CeleryBeat', 'Module Celery Beat'),
                    ('CommandWorker', 'Module Command')
                ],
                default='User',
                max_length=15),
        ),
        migrations.AddField(
            model_name='rate',
            name='nbu_sell',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='rate',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
