# Generated by Django 4.2.1 on 2023-05-12 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aerodevs', '0006_alter_product_part_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AlterField(
            model_name='product',
            name='part_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
