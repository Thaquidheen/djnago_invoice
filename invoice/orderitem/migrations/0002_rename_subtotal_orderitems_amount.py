# Generated by Django 4.2.5 on 2023-09-29 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orderitem', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitems',
            old_name='Subtotal',
            new_name='Amount',
        ),
    ]
