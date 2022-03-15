# Generated by Django 4.0.3 on 2022-03-15 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_content', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Project',
            },
        ),
    ]
