# Generated by Django 2.2 on 2020-10-19 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200318_0924'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('reviewer', 'reviewee')},
        ),
    ]
