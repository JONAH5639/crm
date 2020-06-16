# Generated by Django 3.0.4 on 2020-05-14 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200514_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tags',
        ),
        migrations.AddField(
            model_name='products',
            name='tags',
            field=models.ManyToManyField(to='accounts.Tag'),
        ),
    ]
