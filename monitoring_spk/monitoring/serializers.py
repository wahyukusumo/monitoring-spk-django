from rest_framework import routers, serializers, viewsets
from .models import Amandemen, Keuangan, Pengadaan, Pengawasan


class PengadaanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pengadaan
        fields = ['id', 'bagian', 'nomor_spk', 'vendor', 'tanggal_mulai', 'tanggal_akhir', 'uraian', 'nilai', 'basket', 'status_approval', 'status_bayar']