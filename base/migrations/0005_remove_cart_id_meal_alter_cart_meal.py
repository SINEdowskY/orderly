# Generated by Django 4.0 on 2021-12-29 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_cart_id_meal_alter_cart_meal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='id_meal',
        ),
        migrations.AlterField(
            model_name='cart',
            name='meal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.meal'),
        ),
    ]
