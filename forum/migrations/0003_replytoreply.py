# Generated by Django 3.0.8 on 2020-12-03 04:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0002_auto_20201201_0258'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReplyToReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Reply')),
            ],
            options={
                'verbose_name': 'reply on reply',
                'verbose_name_plural': 'replies on reply',
            },
        ),
    ]