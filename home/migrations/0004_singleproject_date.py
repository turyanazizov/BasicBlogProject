# Generated by Django 4.0.3 on 2022-03-15 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_singleproject'),
    ]

    operations = [
        migrations.AddField(
            model_name='singleproject',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
