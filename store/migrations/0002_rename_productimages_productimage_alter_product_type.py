# Generated by Django 5.1.5 on 2025-01-19 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductImages',
            new_name='ProductImage',
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('shoes', 'Обувь'), ('clothes', 'Одежда'), ('accessories', 'Аксессуары')], max_length=255),
        ),
    ]
