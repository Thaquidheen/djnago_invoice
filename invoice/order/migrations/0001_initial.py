# Generated by Django 4.2.5 on 2023-09-29 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0002_alter_addcustomer_customer_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('OrderID', models.AutoField(primary_key=True, serialize=False)),
                ('OrderDate', models.DateField()),
                ('TotalAmount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.addcustomer')),
            ],
        ),
    ]
