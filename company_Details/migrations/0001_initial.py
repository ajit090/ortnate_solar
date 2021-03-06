# Generated by Django 3.2.7 on 2021-12-22 11:15

from django.db import migrations, models
import gst_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_Name', models.CharField(max_length=100)),
                ('Company_Email', models.EmailField(max_length=100)),
                ('Alternative_Email', models.EmailField(max_length=200)),
                ('Mobile_no', models.IntegerField(max_length=100)),
                ('Alternative_Mobile_no', models.IntegerField(max_length=100)),
                ('GSTN', gst_field.modelfields.GSTField(max_length=15)),
                ('PAN_No', gst_field.modelfields.PANField(max_length=10)),
                ('Lead_source', models.CharField(choices=[('1', 'Team Referal'), ('2', 'tele'), ('3', 'Inbound call'), ('4', 'Mailchimp'), ('5', 'Inbound Email'), ('6', 'Outbound call'), ('7', 'Website'), ('8', 'IndiaMart')], default='1', max_length=20)),
                ('Adress', models.CharField(max_length=200)),
                ('Area', models.CharField(max_length=100)),
                ('City', models.CharField(choices=[('1', 'delhi'), ('2', 'Patna'), ('3', 'pune')], default='1', max_length=50)),
                ('PINCODE', models.IntegerField(max_length=100)),
                ('WEBSITE', models.URLField(max_length=500)),
                ('OWNER', models.CharField(choices=[('1', 'Ajit'), ('2', 'pratik'), ('3', 'abhishek')], default='1', max_length=50)),
            ],
        ),
    ]
