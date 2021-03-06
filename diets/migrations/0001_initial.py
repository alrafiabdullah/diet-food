# Generated by Django 3.1.7 on 2021-03-29 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageAlbum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('ingredients', models.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageCDN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=500)),
                ('url', models.URLField(default='https://ik.imagekit.io/alrafiabdullah/default-image.jpg')),
                ('thumbnail', models.URLField()),
                ('file_type', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='diets.imagealbum')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=250)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('calorie_count', models.PositiveIntegerField(default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('nutritions', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='diets.nutrition')),
                ('photo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='diets.imagealbum')),
            ],
        ),
        migrations.CreateModel(
            name='Custom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=500)),
                ('description', models.TextField(default='', max_length=9999)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('foods', models.ManyToManyField(blank=True, to='diets.Food')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=500)),
                ('description', models.TextField(default='', max_length=9999)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('foods', models.ManyToManyField(blank=True, to='diets.Food')),
            ],
        ),
    ]
