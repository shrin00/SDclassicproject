# Generated by Django 3.0.7 on 2020-06-30 16:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('userdetails', '0004_auto_20200625_1724'),
    ]

    operations = [
        migrations.CreateModel(
            name='news_update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=255, null=True)),
                ('news', models.TextField(blank=True, null=True)),
                ('time', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('water_dep', models.BooleanField(default=False)),
                ('elec_dept', models.BooleanField(default=False)),
                ('road_dept', models.BooleanField(default=False)),
            ],
        ),
    ]