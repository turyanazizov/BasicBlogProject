# Generated by Django 4.0.3 on 2022-03-16 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_abc'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ABC',
            new_name='Blog',
        ),
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'Blog', 'verbose_name_plural': 'Blog'},
        ),
    ]