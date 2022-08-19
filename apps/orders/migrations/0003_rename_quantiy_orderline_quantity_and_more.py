# Generated by Django 4.1 on 2022-08-18 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_order_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="orderline",
            old_name="quantiy",
            new_name="quantity",
        ),
        migrations.AlterField(
            model_name="order",
            name="created_at",
            field=models.DateField(auto_now_add=True),
        ),
    ]