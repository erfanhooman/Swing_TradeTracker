# Generated by Django 5.1.5 on 2025-02-13 07:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_alter_transaction_transaction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_date',
            field=models.DateField(default=datetime.datetime(2025, 2, 13, 7, 10, 0, 200773, tzinfo=datetime.timezone.utc)),
        ),
    ]
