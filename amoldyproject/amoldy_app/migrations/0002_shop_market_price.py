# Generated by Django 3.2 on 2023-03-23 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amoldy_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='market_price',
            field=models.FloatField(default=12, verbose_name='Market Price'),
            preserve_default=False,
        ),
    ]