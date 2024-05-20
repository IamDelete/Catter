# Generated by Django 5.0.3 on 2024-05-19 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catter_index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='elo',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cat',
            name='cat_image',
            field=models.ImageField(upload_to='cats_img/'),
        ),
    ]
