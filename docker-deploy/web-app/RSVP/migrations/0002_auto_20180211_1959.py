# Generated by Django 2.0.1 on 2018-02-12 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RSVP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('Multi', 'Multiple Choice Question'), ('Free', 'Free Text Question')], max_length=100),
        ),
        migrations.AlterField(
            model_name='role',
            name='roleType',
            field=models.CharField(choices=[('vendor', 'vendor'), ('guest', 'guest'), ('owner', 'owner')], max_length=100),
        ),
    ]