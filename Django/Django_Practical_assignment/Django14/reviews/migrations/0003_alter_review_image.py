# Generated by Django 3.2.18 on 2023-04-12 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_alter_review_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
