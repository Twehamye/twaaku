# Generated by Django 4.2.5 on 2023-09-25 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twaaku_app', '0008_otherincome_person_responsible_alter_expense_branch_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otherincome',
            name='person_responsible',
        ),
        migrations.AddField(
            model_name='otherincome',
            name='added_by',
            field=models.CharField(default='EMP001', max_length=50),
        ),
    ]
