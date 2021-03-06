# Generated by Django 3.0.3 on 2020-04-27 12:26

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('emaskjp', '0008_auto_20200427_2114'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplyRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin_date', models.DateField()),
                ('request_qty', models.DecimalField(decimal_places=6, max_digits=16)),
                ('last_update', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('last_calculated', models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 26, 21, 25, 59, 212678), null=True)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emaskjp.Entity')),
            ],
            options={
                'unique_together': {('entity', 'begin_date')},
            },
        ),
        migrations.DeleteModel(
            name='Request',
        ),
    ]
