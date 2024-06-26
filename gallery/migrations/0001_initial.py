# Generated by Django 5.0.1 on 2024-01-29 12:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('image', models.ImageField(upload_to='art_photos/')),
                ('description', models.TextField()),
                ('availability', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('payment', models.CharField(max_length=20)),
                ('artwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.artwork')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.customuser')),
            ],
        ),
    ]
