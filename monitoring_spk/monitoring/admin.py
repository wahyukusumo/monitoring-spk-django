from django.contrib import admin
from .models import Pengadaan, Keuangan, Amandemen, Pengawasan

# Register your models here.
class PengadaanAdmin(admin.ModelAdmin):
    list_display = ('nomor_spk', 'bagian', 'vendor', 'tanggal_mulai', 'tanggal_akhir', 'uraian', 'nilai', 'basket', 'status_approval', 'status_bayar')
    list_per_page = 20


class KeuanganAdmin(admin.ModelAdmin):
    list_display = ('nomor_spk', 'pembayaran', 'nilai', 'tanggal_pembayaran', 'keterangan')
    list_per_page = 20


class AmandemenAdmin(admin.ModelAdmin):
    list_per_page = 20


class PengawasanAdmin(admin.ModelAdmin):
    list_per_page = 20


admin.site.register(Pengadaan, PengadaanAdmin)
admin.site.register(Keuangan, KeuanganAdmin)
admin.site.register(Amandemen, AmandemenAdmin)
admin.site.register(Pengawasan, PengawasanAdmin)
