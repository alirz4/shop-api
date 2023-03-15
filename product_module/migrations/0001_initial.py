# Generated by Django 4.1.7 on 2023-03-14 01:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Category')),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/products', verbose_name='Image')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('off_price', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Discount')),
                ('color', models.CharField(max_length=30, verbose_name='Color')),
                ('is_available', models.BooleanField(default=True)),
                ('category', models.ManyToManyField(blank=True, to='product_module.category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('2XL', '2XL')], max_length=10, verbose_name='Size')),
                ('stoke', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Stoke')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='size', to='product_module.products', verbose_name='Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/gallery', verbose_name='Image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='product_module.products', verbose_name='Product')),
            ],
        ),
    ]
