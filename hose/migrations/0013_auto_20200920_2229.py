# Generated by Django 3.1.1 on 2020-09-20 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hose', '0012_auto_20200912_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_pictiure',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='title',
            field=models.CharField(choices=[('Mr.', 'Mr'), ('Mrs', 'Mrs'), ('Miss', 'Miss'), ('Prof', 'Prof'), ('Engr', 'Engr')], max_length=10, null=True),
        ),
    ]
