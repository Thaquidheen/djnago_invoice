# Generated by Django 4.2.5 on 2023-09-20 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('additem', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item',
            new_name='item_name',
        ),
    ]
