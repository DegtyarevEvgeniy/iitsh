# Generated by Django 4.0.2 on 2023-02-10 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cabinet',
            name='name',
            field=models.CharField(default=0, max_length=200),
        ),
    ]