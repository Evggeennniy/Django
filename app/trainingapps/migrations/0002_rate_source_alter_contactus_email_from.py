# Generated by Django 4.0.6 on 2022-08-25 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trainingapps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='source',
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='trainingapps.source'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='email_from',
            field=models.EmailField(
                choices=[('eugenepavlov@gmail.com', 'eugenepavlov@gmail.com')],
                default='eugenepavlov@gmail.com',
                max_length=30),
        ),
    ]