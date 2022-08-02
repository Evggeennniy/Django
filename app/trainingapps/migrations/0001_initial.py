# Generated by Django 4.0.6 on 2022-08-02 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_from', models.EmailField(max_length=30)),
                ('email_to', models.EmailField(max_length=30)),
                ('subject', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ccy', models.CharField(
                    choices=[
                        ('UAH', 'Hhivna'),
                        ('USD', 'United States Dollar'),
                        ('EUR', 'Euro'),
                        ('BIT', 'Bitcoin')],
                    max_length=5)),
                ('base_ccy', models.CharField(
                    choices=[
                        ('UAH', 'Hhivna'),
                        ('USD', 'United States Dollar'),
                        ('EUR', 'Euro'),
                        ('BIT', 'Bitcoin')],
                    default='UAH',
                    max_length=5)),
                ('buy', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sell', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_url', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
    ]
