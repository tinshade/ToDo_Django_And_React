# Generated by Django 3.0.2 on 2020-08-20 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_autodata_bulkupload'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulkupload',
            name='author',
            field=models.CharField(default='Abhishek', max_length=20),
        ),
    ]
