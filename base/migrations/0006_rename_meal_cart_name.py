# Generated by Django 4.0 on 2021-12-29 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_cart_id_meal_alter_cart_meal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='meal',
            new_name='name',
        ),
    ]
