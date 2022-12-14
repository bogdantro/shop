# Generated by Django 3.1.5 on 2021-02-20 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20210220_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category',
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='none', upload_to=''),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Gaming', 'Gaming'), ('Bogdan', 'Bogdan'), ('Test', 'Test')], max_length=60),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Gaming', 'Gaming'), ('Bogdan', 'Bogdan'), ('Test', 'Test')], max_length=60),
        ),
    ]
