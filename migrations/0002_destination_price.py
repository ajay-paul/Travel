# Generated by Django 3.2.7 on 2021-10-14 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travallo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
