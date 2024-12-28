# Generated by Django 4.2.16 on 2024-11-09 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mode_lam', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vi_tri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vi_tri_lam', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='nhan_vien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tuoi', models.IntegerField()),
                ('gioi_tinh', models.CharField()),
                ('mode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='quan_li_nhan_su.mode')),
                ('vi_tri', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='quan_li_nhan_su.vi_tri')),
            ],
        ),
    ]