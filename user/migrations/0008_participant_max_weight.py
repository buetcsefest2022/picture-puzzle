# Generated by Django 4.0.5 on 2022-06-24 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_participant_batch'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='max_weight',
            field=models.DecimalField(decimal_places=12, default=0, max_digits=30),
        ),
    ]