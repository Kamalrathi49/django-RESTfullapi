# Generated by Django 3.2.6 on 2021-08-28 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='name',
            new_name='book_name',
        ),
    ]