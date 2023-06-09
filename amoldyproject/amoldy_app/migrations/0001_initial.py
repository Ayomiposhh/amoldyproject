# Generated by Django 3.2 on 2023-03-23 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(max_length=300, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=300, unique=True)),
                ('price', models.FloatField(verbose_name='Price')),
                ('author', models.CharField(default='admin', max_length=300)),
                ('in_stock', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('new_product', models.BooleanField(blank=True, null=True, verbose_name='New Product')),
                ('hot_deal', models.BooleanField(blank=True, null=True, verbose_name='Hot Deals of this Week')),
                ('featured', models.BooleanField(blank=True, null=True, verbose_name='Featured')),
                ('best_seller', models.BooleanField(blank=True, default=False, null=True)),
                ('image1', models.ImageField(default='images/default.png', upload_to='images/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('contents', tinymce.models.HTMLField(verbose_name='Content')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='amoldy_app.categories')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ('-created',),
            },
        ),
    ]
