# Generated by Django 3.2.10 on 2021-12-10 09:15

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
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_type', models.SmallIntegerField(choices=[(0, 'Technical'), (1, 'Product'), (2, 'Operations'), (3, 'Design')], verbose_name='JOB type')),
                ('job_name', models.CharField(max_length=250, verbose_name='JOB name')),
                ('job_city', models.SmallIntegerField(choices=[(0, 'Beijing'), (1, 'Shanghai'), (2, 'Shenzhen')], verbose_name='JOB City')),
                ('jobs_reponsibility', models.TextField(max_length=1024, verbose_name='JOB Reponsibility')),
                ('job_requirement', models.TextField(max_length=200, verbose_name='JOB Requirement')),
                ('created_date', models.DateTimeField(verbose_name='Created Date')),
                ('modified_date', models.DateTimeField(verbose_name='Modified Date')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
            ],
        ),
    ]
