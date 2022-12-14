# Generated by Django 3.2.12 on 2022-08-11 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchiveImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField(null=True)),
                ('title', models.CharField(max_length=20)),
                ('contents', models.TextField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArchiveVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_url', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField(null=True)),
                ('title', models.CharField(max_length=20)),
                ('contents', models.TextField(max_length=200, null=True)),
            ],
        ),
    ]
