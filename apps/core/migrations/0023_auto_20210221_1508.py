# Generated by Django 3.1.5 on 2021-02-21 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20210221_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='none', upload_to=''),
        ),
    ]
