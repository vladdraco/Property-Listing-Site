# Generated by Django 3.1.1 on 2020-09-21 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hose', '0013_auto_20200920_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='username',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pictiure',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]