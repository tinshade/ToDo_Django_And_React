# Generated by Django 3.0.2 on 2020-08-20 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200820_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=40)),
                ('bio', models.TextField(max_length=200)),
                ('is_active', models.BooleanField(default=False)),
                ('phone', models.IntegerField()),
                ('email_id', models.EmailField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BulkUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bulkfile', models.FileField(upload_to='Bulk/')),
                ('is_uploaded', models.BooleanField(default=False)),
                ('uploaded_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
