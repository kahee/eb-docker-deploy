# Generated by Django 2.0.3 on 2018-03-13 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_user_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]