# Generated by Django 4.2.1 on 2023-06-19 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.PositiveIntegerField()),
                ('order_id', models.PositiveIntegerField()),
                ('payment_method', models.CharField(max_length=90)),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('transaction_id', models.PositiveIntegerField()),
            ],
        ),
    ]