# Generated by Django 5.1 on 2024-08-24 07:03

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='full name')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='phone number')),
            ],
            options={
                'verbose_name': 'Web Order',
                'verbose_name_plural': 'Web Orders',
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('desc', models.TextField(verbose_name='description')),
                ('percentage', models.PositiveIntegerField(default=0, verbose_name='percentage')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images_discount', to='common.media')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('desc', models.TextField(verbose_name='description')),
                ('size', models.DecimalField(decimal_places=1, help_text='size in liters', max_digits=5, verbose_name='size')),
                ('price', models.DecimalField(decimal_places=2, default=0, help_text="price in so'm", max_digits=10, verbose_name='price')),
                ('discount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.discount')),
                ('image', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='common.media')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('value', models.CharField(max_length=255, verbose_name='value')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='product.product')),
            ],
            options={
                'verbose_name': 'Product Attribute',
                'verbose_name_plural': 'Product Attributes',
            },
        ),
    ]
