# Generated by Django 3.2.12 on 2022-08-04 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('story_id', models.IntegerField(primary_key=True, serialize=False)),
                ('narr_link', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
    ]