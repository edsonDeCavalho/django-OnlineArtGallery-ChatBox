# Generated by Django 4.0.2 on 2022-03-01 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=350)),
                ('productID', models.CharField(max_length=350)),
                ('price', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('img', models.CharField(max_length=1000)),
            ],
        ),
    ]
