# Generated by Django 4.2.5 on 2023-10-17 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('additem', '0003_remove_item_customer_remove_item_rate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemattribute',
            name='currency',
        ),
    ]
