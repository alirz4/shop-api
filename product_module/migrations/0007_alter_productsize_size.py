# Generated by Django 4.1.7 on 2023-03-19 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0006_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsize',
            name='size',
            field=models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('2XL', '2XL'), ('3XL', '3XL')], max_length=10, verbose_name='Size'),
        ),
    ]
