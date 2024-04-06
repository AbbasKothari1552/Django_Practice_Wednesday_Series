# Generated by Django 5.0.4 on 2024-04-06 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='phone_no',
            field=models.IntegerField(blank=True, verbose_name='Contact Number'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='website',
            field=models.CharField(blank=True, max_length=100, verbose_name='Website Address'),
        ),
    ]