# Generated by Django 4.0.2 on 2022-03-01 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_rename_userid_profile_productid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='views',
            field=models.IntegerField(default=5, max_length=100),
            preserve_default=False,
        ),
    ]
