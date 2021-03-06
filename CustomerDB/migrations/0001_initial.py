# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-16 08:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('cluster_id', models.AutoField(primary_key=True, serialize=False)),
                ('cluster_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('contact_person', models.CharField(max_length=200)),
                ('contact_phone', models.CharField(max_length=15)),
                ('contact_mobile', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('contract_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=200, unique=True)),
                ('ras_procedure', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='HardWare',
            fields=[
                ('model_id', models.AutoField(primary_key=True, serialize=False)),
                ('model_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('node_id', models.AutoField(primary_key=True, serialize=False)),
                ('node_name', models.CharField(max_length=30)),
                ('hw_models', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CustomerDB.HardWare')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=15, unique=True)),
                ('role_description', models.CharField(default='contact role', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Third_party',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('ticket_link', models.URLField(null=True)),
                ('company_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('version_id', models.AutoField(primary_key=True, serialize=False)),
                ('version_name', models.CharField(max_length=20)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CustomerDB.Product')),
            ],
        ),
        migrations.AddField(
            model_name='hardware',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CustomerDB.Third_party'),
        ),
        migrations.AddField(
            model_name='contract',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CustomerDB.Customer'),
        ),
        migrations.AddField(
            model_name='contract',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CustomerDB.Product'),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CustomerDB.Customer'),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CustomerDB.Roles'),
        ),
        migrations.AddField(
            model_name='cluster',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CustomerDB.Contract'),
        ),
        migrations.AddField(
            model_name='cluster',
            name='version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CustomerDB.Version'),
        ),
    ]
