# Generated by Django 5.1.4 on 2025-01-04 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0006_rename_student_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='year_in_school',
        ),
        migrations.AddField(
            model_name='seller',
            name='year_in_university',
            field=models.CharField(choices=[('1', '1 курс'), ('2', '2 курс'), ('3', '3 курс'), ('4', '4 курс'), ('5', '5 курс')], default='1', max_length=2),
        ),
    ]
