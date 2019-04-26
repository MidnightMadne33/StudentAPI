# Generated by Django 2.2 on 2019-04-26 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gpa',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='student',
            name='has_graduated',
            field=models.BooleanField(default=False, verbose_name='Has the student graduated?'),
        ),
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(choices=[('IT', 'Information Technology'), ('MAE', 'Mechanical and Automation Engineering'), ('CSE', 'Computer Science Enginnering'), ('EEE', 'Electronics and Electrical Engineering'), ('ECE', 'Electronics and Communication Engineering')], default='--', max_length=3),
        ),
        migrations.AlterField(
            model_name='student',
            name='degree',
            field=models.CharField(default='B.Tech', max_length=20),
        ),
    ]
