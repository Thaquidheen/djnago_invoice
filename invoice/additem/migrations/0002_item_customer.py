# Generated by Django 4.2.5 on 2023-10-10 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('additem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='customer.addcustomer'),
            preserve_default=False,
        ),
    ]
