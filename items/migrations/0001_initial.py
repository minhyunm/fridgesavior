# Generated by Django 4.1.1 on 2022-12-11 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('expire_within', models.PositiveSmallIntegerField(default=0)),
                ('detail', models.TextField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.productcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expired_at', models.DateField()),
                ('amount', models.PositiveSmallIntegerField(default=0)),
                ('unit', models.CharField(max_length=10)),
                ('detail', models.TextField(null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.product')),
            ],
        ),
    ]