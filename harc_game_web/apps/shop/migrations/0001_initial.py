# Generated by Django 3.1.3 on 2020-12-02 19:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(help_text='Można używać tagów HTML', verbose_name='Opis zapotrzebowania')),
                ('link1', models.CharField(blank=True, default='', max_length=400, null=True, verbose_name='Link 1')),
                ('link2', models.CharField(blank=True, default='', max_length=400, null=True, verbose_name='Link 2')),
                ('link3', models.CharField(blank=True, default='', max_length=400, null=True, verbose_name='Link 3')),
                ('price', models.IntegerField(default=0, null=True, verbose_name='Cena')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Na kiedy jest to potrzebne')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'prośba',
                'verbose_name_plural': 'log próśb',
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='shop.request')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'głos na prośbę',
                'verbose_name_plural': 'głosy na prośby',
            },
        ),
    ]
