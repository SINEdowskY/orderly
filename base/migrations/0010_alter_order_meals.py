# Generated by Django 4.0 on 2021-12-30 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_rename_cost_order_costs_remove_order_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='meals',
            field=models.JSONField(default=dict),
        ),
    ]
