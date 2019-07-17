# Generated by Django 2.2.2 on 2019-07-17 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('material', '0002_resinlabel'),
        ('columnstatictis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PressureandVelocity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packingproject', models.CharField(blank=True, max_length=20, verbose_name='装柱项目')),
                ('columnid', models.CharField(blank=True, max_length=50, verbose_name='层析柱编号')),
                ('resinid', models.CharField(blank=True, max_length=50, verbose_name='填料编号')),
                ('minipackingvelocity', models.CharField(blank=True, max_length=20, verbose_name='最低装柱流速')),
                ('maxpackingvelocity', models.CharField(blank=True, max_length=20, verbose_name='最高装柱流速')),
                ('packingpressure', models.CharField(blank=True, max_length=20, verbose_name='装柱压力')),
                ('productionvelocity', models.CharField(blank=True, max_length=20, verbose_name='生产流速')),
                ('columnheight', models.CharField(blank=True, max_length=20, verbose_name='柱高')),
                ('columndimeter', models.CharField(blank=True, max_length=20, verbose_name='层析柱直径')),
                ('symmetry', models.CharField(blank=True, max_length=20, verbose_name='对称性')),
                ('hetp', models.CharField(blank=True, max_length=20, verbose_name='HETP')),
                ('comment', models.CharField(blank=True, max_length=1000, verbose_name='备注')),
                ('resin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materisesin', to='material.ResinLabel', verbose_name='填料id')),
            ],
        ),
    ]
