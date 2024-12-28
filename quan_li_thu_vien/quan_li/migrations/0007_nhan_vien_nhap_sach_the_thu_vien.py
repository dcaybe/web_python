# Generated by Django 4.2.16 on 2024-09-26 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quan_li', '0006_delete_mymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='nhan_vien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_nv', models.IntegerField()),
                ('ten_nv', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='nhap_sach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_nhap', models.IntegerField()),
                ('ma_sach', models.IntegerField()),
                ('ma_nv', models.IntegerField()),
                ('ngay_nhap', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='the_thu_vien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_the', models.IntegerField()),
                ('ma_sv', models.IntegerField()),
                ('ngay_lap', models.DateField()),
            ],
        ),
    ]
