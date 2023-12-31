# Generated by Django 4.2.3 on 2023-07-22 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0005_alter_pengadaan_basket_alter_pengadaan_nilai_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pengadaan',
            name='bagian',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='pengadaan',
            name='basket',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='pengadaan',
            name='nilai',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='pengadaan',
            name='nomor_spk',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='pengadaan',
            name='status_approval',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='pengadaan',
            name='status_bayar',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='pengadaan',
            name='tanggal_akhir',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pengadaan',
            name='tanggal_mulai',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pengadaan',
            name='uraian',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='pengadaan',
            name='vendor',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
