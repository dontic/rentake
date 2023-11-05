# Generated by Django 4.2.7 on 2023-11-05 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('catastral_reference', models.CharField(max_length=200)),
                ('storage_room_number', models.CharField(blank=True, max_length=200, null=True)),
                ('number_of_bedrooms', models.IntegerField()),
                ('number_of_bathrooms', models.IntegerField()),
                ('address_line_1', models.CharField(max_length=200)),
                ('address_line_2', models.CharField(blank=True, max_length=200, null=True)),
                ('postcode', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('province', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('is_rented', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=200)),
                ('floor', models.IntegerField()),
                ('address_line_1', models.CharField(max_length=200)),
                ('address_line_2', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(max_length=200)),
                ('province', models.CharField(max_length=200)),
                ('postcode', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('is_rented', models.BooleanField(default=False)),
                ('associated_property', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='realestate.property')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('rent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('deposit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_active', models.BooleanField(default=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='contracts')),
                ('parkings', models.ManyToManyField(blank=True, to='realestate.parking')),
                ('property', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='realestate.property')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realestate.tenant')),
            ],
        ),
    ]
