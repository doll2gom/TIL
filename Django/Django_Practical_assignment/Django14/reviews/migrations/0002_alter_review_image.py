# Generated by Django 3.2.18 on 2023-04-12 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d/'),
        ),
    ]