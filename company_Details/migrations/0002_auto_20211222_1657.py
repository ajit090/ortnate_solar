# Generated by Django 3.2.7 on 2021-12-22 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_Details', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='Alternative_Mobile_no',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='Mobile_no',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='PINCODE',
            field=models.CharField(max_length=100),
        ),
    ]