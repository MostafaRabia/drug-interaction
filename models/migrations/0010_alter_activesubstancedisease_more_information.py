# Generated by Django 4.2.3 on 2023-07-22 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0009_rename_active_substances2_disease_active_substances'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activesubstancedisease',
            name='more_information',
            field=models.CharField(max_length=150, null=True),
        ),
    ]