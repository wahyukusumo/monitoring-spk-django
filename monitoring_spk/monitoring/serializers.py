from rest_framework import routers, serializers, viewsets
from .models import Amandemen, Keuangan, Pengadaan, Pengawasan


class PengadaanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pengadaan
        fields = ['id', 'bagian', 'nomor_spk', 'vendor', 'tanggal_mulai', 'tanggal_akhir', 'uraian', 'nilai', 'basket', 'status_approval', 'status_bayar']


class KeuanganSerializer(serializers.HyperlinkedModelSerializer):
    nomor_spk = PengadaanSerializer(read_only=True)
    nomor_spk_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Keuangan
        fields = ['id', 'pembayaran', 'nilai', 'tanggal_pembayaran', 'keterangan', 'nomor_spk_id', 'nomor_spk']


class PengawasanSerializer(serializers.HyperlinkedModelSerializer):
    nomor_spk = PengadaanSerializer(read_only=True)
    nomor_spk_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Pengawasan
        fields = ['nomor_spk', 'progress', 'a3c_150', 'a3c_240', 'mvtic_150', 'mvtic_240', 'xlpe_240', 'xlpe_300', 'trafo_100kva', 'trafo_160kva', 'trafo_200kva', 'trafo_250kva', 'trafo_315kva', 'trafo_400kva', 'trafo_630kva', 'trafo_1000kva', 'jtr_rak_tr', 'jtr_sktr', 'tic_3x70', 'tic_3x95', 'tic_2x10', 'tic_2x16', 'air_insulated_lbs', 'air_insulated_pb', 'air_insulated_cbom', 'fully_insulated_lbs', 'fully_insulated_pb', 'fully_insulated_cbom', 'kubikel_gi_incoming', 'kubikel_gi_kopel', 'kubikel_gi_outgoing', 'kubikel_gi_riser', 'kubikel_gi_cell_vt', 'kubikel_gi_ps', 'kwh_1_phase_prabayar', 'kwh_1_phase_reguler', 'kwh_elektrik_3_phase_kecil', 'kwh_amr_3_phase_besar', 'kwh_amr_3_phase_tm', 'phase_1_2a', 'phase_1_4a', 'phase_1_6a', 'phase_1_10a', 'phase_1_16a', 'phase_1_25a', 'phase_1_35a', 'phase_1_50a', 'phase_3_10a', 'phase_3_16a', 'phase_3_20a', 'phase_3_25a', 'phase_3_35a', 'phase_3_50a', 'mccb_63', 'mccb_80', 'mccb_100', 'mccb_150', 'mccb_200', 'mccb_250', 'mccb_300', 'keterangan', 'rencana_bayar']