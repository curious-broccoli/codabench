# Generated by Django 2.2.13 on 2020-07-24 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0015_auto_20200710_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submission', to='datasets.Data'),
        ),
    ]
