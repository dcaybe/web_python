# Generated by Django 4.2.16 on 2024-11-23 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quan_li_quan_game', '0002_alter_computer_computer_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_user', models.CharField(max_length=20)),
                ('password', models.CharField()),
                ('balance', models.FloatField()),
            ],
        ),
    ]
