# Generated by Django 2.2.2 on 2019-08-30 08:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('ihr', '0034_auto_20190628_0645'),
    ]

    operations = [
        migrations.CreateModel(
            name='IHRUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='atlas_delay',
            name='endpoint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location_endpoint', to='ihr.Atlas_location'),
        ),
        migrations.AlterField(
            model_name='atlas_delay',
            name='startpoint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location_startpoint', to='ihr.Atlas_location'),
        ),
        migrations.CreateModel(
            name='MonitoredASN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notifylevel', models.SmallIntegerField(choices=[(0, 'low'), (5, 'moderate'), (10, 'high')], default=10)),
                ('asn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ihr.ASN')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmailChangeRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_email', models.EmailField(max_length=254, unique=True)),
                ('request_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ihruser',
            name='monitoringasn',
            field=models.ManyToManyField(through='ihr.MonitoredASN', to='ihr.ASN'),
        ),
        migrations.AddField(
            model_name='ihruser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
