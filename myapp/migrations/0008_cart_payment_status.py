# Generated by Django 4.0.2 on 2022-03-05 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
    ]
