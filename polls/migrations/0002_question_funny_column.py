# Generated by Django 3.1.3 on 2021-09-12 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='funny_column',
            field=models.CharField(max_length=10, null=True),
        ),
    ]