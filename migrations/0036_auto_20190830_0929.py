# Generated by Django 2.2.2 on 2019-08-30 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ihr', '0035_auto_20190830_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailchangerequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ihr.IHRUser'),
        ),
        migrations.AlterField(
            model_name='ihruser',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='ihruser_set', related_query_name='ihruser', to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='ihruser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='ihruser_set', related_query_name='ihruser', to='auth.Permission'),
        ),
        migrations.AlterField(
            model_name='monitoredasn',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ihr.IHRUser'),
        ),
    ]
