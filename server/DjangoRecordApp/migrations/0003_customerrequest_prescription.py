# Generated by Django 3.0.8 on 2023-08-20 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoRecordApp', '0002_auto_20200715_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerrequest',
            name='prescription',
            field=models.FileField(default='', upload_to=''),
        ),
    ]