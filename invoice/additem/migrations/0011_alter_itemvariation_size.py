# Generated by Django 4.2.5 on 2023-10-17 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('additem', '0010_alter_itemvariation_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemvariation',
            name='size',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]