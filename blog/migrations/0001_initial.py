# Generated by Django 4.0.3 on 2022-03-18 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blogs/')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('creator_name', models.CharField(max_length=100)),
                ('creator_img', models.ImageField(upload_to='creators/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('second_title', models.CharField(max_length=255)),
                ('second_content', models.TextField()),
                ('creator_bio', models.TextField()),
                ('creator_job', models.CharField(max_length=105)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blog',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Approve', 'Approve'), ('Reject', 'Reject')], max_length=50)),
                ('text', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='koments', to='blog.blog')),
            ],
        ),
    ]
