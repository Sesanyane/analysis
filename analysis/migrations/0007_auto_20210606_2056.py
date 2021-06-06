# Generated by Django 3.1.4 on 2021-06-06 20:56

import _socket
from django.db import migrations, models
import django_revision.revision_field
import edc_base.model_fields.hostname_modification_field
import edc_base.model_fields.userfield
import edc_base.model_fields.uuid_auto_field
import edc_base.utils


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0006_auto_20210606_2035'),
    ]

    operations = [
        migrations.CreateModel(
            name='LearnVaccine',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('short_name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
            ],
            options={
                'ordering': ['display_index', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('short_name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
            ],
            options={
                'ordering': ['display_index', 'name'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='ruralcommunityrapidassessment',
            name='covid19_learning',
        ),
        migrations.RemoveField(
            model_name='ruralcommunityrapidassessment',
            name='role',
        ),
        migrations.AddField(
            model_name='ruralcommunityrapidassessment',
            name='covid19_learning',
            field=models.ManyToManyField(blank=True, max_length=100, to='analysis.LearnVaccine', verbose_name='If yes, where did you learn about Coronavirus/COVID-19 Vaccine?'),
        ),
        migrations.AddField(
            model_name='ruralcommunityrapidassessment',
            name='role',
            field=models.ManyToManyField(blank=True, max_length=200, to='analysis.Role', verbose_name='What is your current role?'),
        ),
    ]
