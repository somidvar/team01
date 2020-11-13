# Generated by Django 3.1.2 on 2020-11-12 02:06

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0007_delete_buyers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Id', models.IntegerField()),
                ('Budget', models.DecimalField(decimal_places=0, default=Decimal('0'), max_digits=5, validators=[django.core.validators.MinValueValidator(1)])),
                ('Spent', models.DecimalField(decimal_places=0, default=Decimal('0'), max_digits=5, validators=[django.core.validators.MinValueValidator(1)])),
            ],
            options={
                'db_table': 'Buyers',
                'managed': False,
            },
        ),
    ]