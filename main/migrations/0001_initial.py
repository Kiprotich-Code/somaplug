# Generated by Django 4.2.4 on 2024-05-01 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddQuote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.PositiveIntegerField()),
                ('service', models.CharField(max_length=100)),
                ('expected_time', models.CharField(max_length=20)),
                ('details', models.TextField()),
                ('quote', models.IntegerField()),
            ],
        ),
    ]
