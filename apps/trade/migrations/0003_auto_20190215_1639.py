# Generated by Django 2.0.6 on 2019-02-15 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0002_auto_20181212_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='order_sn',
            field=models.CharField(blank=True, default='ordersn', max_length=30, null=True, unique=True, verbose_name='订单号'),
        ),
    ]