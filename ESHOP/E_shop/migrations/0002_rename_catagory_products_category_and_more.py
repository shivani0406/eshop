# Generated by Django 5.0 on 2024-03-06 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('E_shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='catagory',
            new_name='category',
        ),
        migrations.AlterModelTable(
            name='catagories',
            table='category',
        ),
        migrations.AlterModelTable(
            name='products',
            table='products',
        ),
    ]
