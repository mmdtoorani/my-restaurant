# Generated by Django 4.0.1 on 2022-01-31 04:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField(max_length=250)),
                ('city', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=250, null=True)),
                ('created', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('branch', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='restaurant.branch')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('Iranian-restaurant', 'Iranian restaurant'), ('Italian-restaurant', 'Italian restaurant'), ('French-restaurant', 'French restaurant'), ('Chinese-restaurant', 'Chinese restaurant')], help_text='please choose type of restaurant', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personnel_id', models.IntegerField(unique=True)),
                ('type_of_personnel', models.CharField(choices=[('servant', 'servant'), ('waiter', 'waiter'), ('chef', 'chef'), ('manager', 'manager')], help_text='please select a position in personnel', max_length=30)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.branch')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.menu')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restaurant.restaurant'),
        ),
    ]
