# Generated by Django 2.2 on 2020-03-02 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0009_auto_20200302_1549'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advert',
            old_name='ad_pic',
            new_name='image',
        ),
    ]
