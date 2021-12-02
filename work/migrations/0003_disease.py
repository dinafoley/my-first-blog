# Generated by Django 3.2.9 on 2021-12-01 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_diseasetype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('disease_code', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('pathogen', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.CharField(blank=True, max_length=140, null=True)),
            ],
            options={
                'db_table': 'disease',
                'managed': False,
            },
        ),
    ]