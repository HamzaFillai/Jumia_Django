# Generated by Django 4.0 on 2021-12-30 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0004_alter_cluster_idproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cluster',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
