# Generated by Django 2.2 on 2019-05-18 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0026_remove_supplierpart_single_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partattachment',
            name='comment',
            field=models.CharField(help_text='File comment', max_length=100),
        ),
    ]
