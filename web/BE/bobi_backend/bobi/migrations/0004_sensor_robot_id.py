# Generated by Django 3.2.12 on 2022-08-11 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bobi', '0003_auto_20220811_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='robot_id',
            field=models.ForeignKey(db_column='robot_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sensors', to='bobi.robot'),
        ),
    ]
