# Generated by Django 4.1.7 on 2023-03-18 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0005_remove_products_is_favorite_productfavorite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('image', models.ImageField(upload_to='banners', verbose_name='Image')),
                ('description', models.TextField()),
                ('location', models.CharField(choices=[('SW', 'SW'), ('SW1', 'SW1'), ('SW2', 'SW2')], max_length=30, verbose_name='Location')),
            ],
        ),
    ]