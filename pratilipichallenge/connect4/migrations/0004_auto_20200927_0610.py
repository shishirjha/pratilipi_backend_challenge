# Generated by Django 3.1.1 on 2020-09-27 00:40

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect4', '0003_auto_20200927_0608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='board',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('Y', 'First Player'), ('R', 'Second Player')], default='X', max_length=1, null=True), null=True, size=7), null=True, size=6),
        ),
    ]
