# Generated by Django 2.2.2 on 2019-07-17 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('columnstatictis', '0002_pressureandvelocity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pressureandvelocity',
            options={'permissions': [('black_article', '拉黑压力流速表的权限')]},
        ),
    ]
