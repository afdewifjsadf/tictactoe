# Generated by Django 3.2.8 on 2021-10-25 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_delete_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='bot',
            name='level',
            field=models.CharField(blank=True, choices=[('B', 'BEGINNER'), ('I', 'INTERMEDIATE'), ('A', 'ADVANCED')], max_length=5, null=True),
        ),
    ]