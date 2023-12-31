# Generated by Django 4.2.1 on 2023-06-19 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ordering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.PositiveIntegerField()),
                ('products', models.CharField(max_length=90)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('shipping_address', models.CharField(max_length=90)),
                ('order_date', models.DateField()),
            ],
        ),
    ]
