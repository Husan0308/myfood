# Generated by Django 5.0.4 on 2024-05-12 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streetfood', '0002_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
