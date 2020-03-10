# Generated by Django 2.2.2 on 2020-01-21 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ihr', '0037_auto_20190918_0011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hegemony_alarms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timebin', models.DateTimeField(db_index=True)),
                ('deviation', models.FloatField(default=0.0)),
                ('af', models.IntegerField()),
                ('asn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anomalous_asn', to='ihr.ASN')),
                ('originasn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anomalous_originasn', to='ihr.ASN')),
            ],
        ),
        migrations.CreateModel(
            name='Atlas_delay_alarms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timebin', models.DateTimeField(db_index=True)),
                ('deviation', models.FloatField(default=0.0)),
                ('endpoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anomalous_endpoint', to='ihr.Atlas_location')),
                ('startpoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anomalous_startpoint', to='ihr.Atlas_location')),
            ],
        ),
    ]