# Generated by Django 3.1.7 on 2021-03-29 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagealbum',
            name='name',
            field=models.CharField(default='First', max_length=500, unique=True),
            preserve_default=False,
        ),
    ]