# Generated by Django 5.1.3 on 2024-12-15 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_alter_account_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verification',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='verification',
            name='expired_at',
            field=models.DateTimeField(null=True),
        ),
    ]
