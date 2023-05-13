# Generated by Django 4.2.1 on 2023-05-13 08:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aerodevs', '0008_merge_20230512_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Buyer', to=settings.AUTH_USER_MODEL)),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aerodevs.product')),
            ],
        ),
    ]