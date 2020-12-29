# Generated by Django 3.0.8 on 2020-12-01 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remitent', models.EmailField(max_length=254, verbose_name='email')),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('img', models.ImageField(blank=True, upload_to='messages/%Y/%m/%d/', verbose_name='picture')),
            ],
        ),
    ]