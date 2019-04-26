# Generated by Django 2.2 on 2019-04-26 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0002_auto_20190426_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='degree',
            field=models.CharField(default='B.Tech', editable=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='gpa',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='has_graduated',
            field=models.BooleanField(verbose_name='Has the student graduated?'),
        ),
    ]