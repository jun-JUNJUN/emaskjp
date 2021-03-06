# Generated by Django 3.0.3 on 2020-04-27 09:24

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('emaskjp', '0006_demand_begin_date_display'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2)])),
                ('prefecture', models.CharField(blank=True, max_length=40, verbose_name='都道府県')),
                ('address1', models.CharField(max_length=40, verbose_name='市区町村番地')),
                ('address2', models.CharField(blank=True, max_length=40, verbose_name='建物名')),
            ],
        ),
        migrations.CreateModel(
            name='SupplierContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emaskjp.Supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin_date', models.DateField()),
                ('supply_qty', models.DecimalField(decimal_places=6, max_digits=16)),
                ('destination_entity', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='emaskjp.Entity')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='emaskjp.Supplier')),
            ],
            options={
                'unique_together': {('destination_entity', 'supplier', 'begin_date')},
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin_date', models.DateField()),
                ('request_qty', models.DecimalField(decimal_places=6, max_digits=16)),
                ('last_update', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('last_calculated', models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 26, 18, 24, 48, 254113), null=True)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emaskjp.Entity')),
            ],
            options={
                'unique_together': {('entity', 'begin_date')},
            },
        ),
    ]
