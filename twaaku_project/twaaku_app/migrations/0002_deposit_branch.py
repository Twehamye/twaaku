# Generated by Django 4.2.5 on 2023-09-22 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twaaku_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='branch',
            field=models.CharField(choices=[('Nateete', 'Nateete'), ('kisenyi', 'kisenyi'), ('Kikajjo', 'Kikajjo'), ('Other', 'Other')], default='Nateete', max_length=200),
        ),
    ]