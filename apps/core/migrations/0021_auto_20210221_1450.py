# Generated by Django 3.1.5 on 2021-02-21 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20210221_1303'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='label',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=10),
        ),
    ]