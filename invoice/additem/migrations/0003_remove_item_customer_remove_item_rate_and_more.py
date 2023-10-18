# Generated by Django 4.2.5 on 2023-10-17 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('additem', '0002_item_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='item',
            name='rate',
        ),
        migrations.RemoveField(
            model_name='item',
            name='rate_currency',
        ),
        migrations.RemoveField(
            model_name='item',
            name='size',
        ),
        migrations.RemoveField(
            model_name='item',
            name='thickness',
        ),
        migrations.CreateModel(
            name='ItemAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=50)),
                ('thickness', models.CharField(max_length=50)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(default='INR', max_length=3)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='additem.item')),
            ],
        ),
    ]
