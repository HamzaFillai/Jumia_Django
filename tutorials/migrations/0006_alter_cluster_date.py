# Generated by Django 4.0 on 2021-12-30 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0005_alter_cluster_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cluster',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
