# Generated by Django 5.1.4 on 2025-01-12 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='available',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]