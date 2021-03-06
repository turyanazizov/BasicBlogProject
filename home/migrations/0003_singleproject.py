# Generated by Django 4.0.3 on 2022-03-15 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_projects_main_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='SingleProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(blank=True, max_length=100, null=True)),
                ('role', models.CharField(blank=True, max_length=100, null=True)),
                ('agency', models.CharField(blank=True, max_length=100, null=True)),
                ('content', models.CharField(blank=True, max_length=100, null=True)),
                ('image1', models.ImageField(upload_to='projects/')),
                ('image2', models.ImageField(upload_to='projects/')),
                ('image3', models.ImageField(upload_to='projects/')),
            ],
            options={
                'verbose_name': 'Single Project',
                'verbose_name_plural': 'Single Projects',
            },
        ),
    ]
