# Generated by Django 2.2.7 on 2019-11-18 12:15

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
            name='Avatar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
                ('force', models.IntegerField(default=100)),
                ('defense', models.IntegerField(default=80)),
                ('life', models.IntegerField(default=1000)),
                ('level', models.IntegerField(default=0)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='avatar_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Knowing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('defense', models.IntegerField(default=0)),
                ('allowed_level', models.IntegerField(default=0)),
                ('avatar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='knowledge', to='game.Avatar')),
            ],
        ),
        migrations.CreateModel(
            name='Abiliity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('force', models.IntegerField(default=0)),
                ('allowed_level', models.IntegerField(default=0)),
                ('avatar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abiliities', to='game.Avatar')),
            ],
        ),
    ]
