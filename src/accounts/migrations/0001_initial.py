# Generated by Django 3.2.9 on 2022-02-07 03:55

import accounts.validators
import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(help_text='Email address must be unique. It is used to login and confirm the account.', max_length=254, unique=True, verbose_name='Email address')),
                ('account_identifier', models.CharField(help_text="Account identifier is used to identify your account. This will be used for bans, job bans, etc and can't ever be changed", max_length=28, primary_key=True, serialize=False, validators=[accounts.validators.AccountNameValidator()], verbose_name='Account identifier')),
                ('username', models.CharField(help_text='Public username is used to identify your account publicly and shows in OOC. This can be changed at any time', max_length=28, validators=[accounts.validators.UsernameValidator()], verbose_name='Public username')),
                ('is_verified', models.BooleanField(default=False, help_text='Is this account verified to be who they claim to be? Are they famous?!', verbose_name='Verified')),
                ('legacy_id', models.CharField(blank=True, default='null', help_text="Legacy ID is used to identify your account in the old database. This is used for bans, job bans, etc and can't ever be changed", max_length=28, verbose_name='Legacy ID')),
                ('characters_data', models.JSONField(default=dict, help_text='Characters data is used to store all the characters associated with this account.', verbose_name='Characters data')),
                ('is_authorized_server', models.BooleanField(default=False, help_text='Can this account broadcast the server state to the server list api? Can this account write to persistence layer?', verbose_name='Authorized server')),
                ('verification_token', models.UUIDField(blank=True, default=uuid.UUID('05e74bff-c4b1-4452-ac03-b20805ac4fef'), verbose_name='Verification token')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
