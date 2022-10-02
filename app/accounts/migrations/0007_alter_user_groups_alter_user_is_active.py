# Generated by Django 4.1 on 2022-10-02 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0006_alter_user_groups_alter_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(
                blank=True,
                help_text='The groups this user belongs to.',
                related_name='user_set',
                related_query_name='user',
                to='auth.group',
                verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(
                default=True,
                help_text='Designates whether this user should be treated as active.',
                verbose_name='active'),
        ),
    ]
