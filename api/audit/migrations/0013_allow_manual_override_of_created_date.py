# Generated by Django 3.2.23 on 2023-12-01 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0012_auto_20230517_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditlog',
            name='created_date',
            field=models.DateTimeField(verbose_name='DateCreated'),
        ),
    ]