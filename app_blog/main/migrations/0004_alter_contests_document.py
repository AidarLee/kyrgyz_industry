# Generated by Django 4.0.8 on 2022-10-11 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_contests_document_contests_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contests',
            name='Document',
            field=models.FileField(upload_to='', verbose_name='Документ'),
        ),
    ]
