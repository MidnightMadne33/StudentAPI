# Generated by Django 2.2 on 2019-04-26 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0004_auto_20190426_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resume'),
        ),
    ]