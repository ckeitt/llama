# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-29 01:31
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicle', '0001_initial'),
        ('rider', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('abbreviated_name', models.CharField(blank=True, max_length=255, null=True)),
                ('area', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('discount_dollar_type', models.BooleanField(default=True)),
                ('discount_percentage_type', models.BooleanField(default=False)),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=10, max_length=10)),
                ('discount_percentage', models.DecimalField(decimal_places=5, default=0, max_digits=10, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('area', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='districts', to='pricing.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('area', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='markets', to='pricing.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activation_fee', models.DecimalField(decimal_places=4, max_digits=10, max_length=10)),
                ('usage_fee', models.DecimalField(decimal_places=4, max_digits=10, max_length=10)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='pricing.Country')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='pricing.District')),
                ('market', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='pricing.Market')),
            ],
        ),
        migrations.CreateModel(
            name='PromotionalCredit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('code', models.CharField(max_length=255)),
                ('max_number_of_uses', models.IntegerField(default=1)),
                ('credit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pricing.Credit')),
            ],
        ),
        migrations.CreateModel(
            name='RiderCredit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
                ('days_available_type', models.BooleanField(default=False)),
                ('usage_number_type', models.BooleanField(default=True)),
                ('max_days_available', models.IntegerField(default=1)),
                ('max_number_of_uses', models.IntegerField(default=1)),
                ('rider_amount_used', models.DecimalField(decimal_places=2, default=0, max_digits=10, max_length=10)),
                ('referring_rider_amount_used', models.DecimalField(decimal_places=2, default=0, max_digits=10, max_length=10)),
                ('referring_rider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referring_credits', to='rider.Rider')),
                ('referring_rider_credit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='pricing.Credit')),
                ('rider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='credits', to='rider.Rider')),
                ('rider_credit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='pricing.Credit')),
            ],
        ),
        migrations.CreateModel(
            name='RiderPromotionalCredit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_times_used', models.IntegerField(default=0)),
                ('promotion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pricing.PromotionalCredit')),
                ('rider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='promotions', to='rider.Rider')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('abbreviated_name', models.CharField(blank=True, max_length=255, null=True)),
                ('area', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='states', to='pricing.Country')),
            ],
        ),
        migrations.AddField(
            model_name='pricing',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='pricing.State'),
        ),
        migrations.AddField(
            model_name='pricing',
            name='vehicle_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pricing', to='vehicle.VehicleType'),
        ),
    ]