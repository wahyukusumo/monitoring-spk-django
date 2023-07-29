from django.shortcuts import render
from django.db.models import Q
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import PengadaanSerializer, KeuanganSerializer, PengawasanSerializer
from .models import Pengadaan, Keuangan, Pengawasan

# Create your views here.

@csrf_exempt
def pengadaan(request):
    if (request.method == 'GET'):
        pengadaan = Pengadaan.objects.all()
        serializers = PengadaanSerializer(pengadaan, many=True)
        return JsonResponse(serializers.data, safe=False)

    elif (request.method == 'POST'):
        data = JSONParser().parse(request)
        serializers = PengadaanSerializer(data = data)
        if (serializers.is_valid()):
            serializers.save()
            return JsonResponse(serializers.data, status=201)

        return JsonResponse(serializers.errors, status=400)

@csrf_exempt
def pengadaan_detail(request, pk):
    try:
        pengadaan = Pengadaan.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if (request.method == 'PUT'):
        data = JSONParser().parse(request)
        serializer = PengadaanSerializer(pengadaan, data=data)

        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

    elif(request.method == 'DELETE'):
        pengadaan.delete()
        return HttpResponse(status=204)

@csrf_exempt
def keuangan(request):
    if (request.method == 'GET'):
        keuangan = Keuangan.objects.all()
        serializers = KeuanganSerializer(keuangan, many=True)
        return JsonResponse(serializers.data, safe=False)

    elif (request.method == 'POST'):
        data = JSONParser().parse(request)
        serializers = KeuanganSerializer(data = data)
        if (serializers.is_valid()):
            serializers.save()
            return JsonResponse(serializers.data, status=201)

        return JsonResponse(serializers.errors, status=400)

@csrf_exempt
def pengawasan(request):
    if (request.method == 'GET'):
        pengawas = Pengawasan.objects.all()
        serializers = PengawasanSerializer(pengawas, many=True)
        return JsonResponse(serializers.data, safe=False)

    elif (request.method == 'POST'):
        data = JSONParser().parse(request)
        serializers = PengawasanSerializer(data = data)
        if (serializers.is_valid()):
            serializers.save()
            return JsonResponse(serializers.data, status=201)

        return JsonResponse(serializers.errors, status=400)

def search(request):
    get_q = request.GET.get('q')
    keywords = get_q.split()

    for keyword in keywords:
        query = Pengadaan.objects.filter(Q(nomor_spk__icontains=keyword) |
                Q(bagian__icontains=keyword) |
                Q(vendor__icontains=keyword) |
                Q(tanggal_mulai__icontains=keyword) |
                Q(tanggal_akhir__icontains=keyword) |
                Q(nilai__icontains=keyword) |
                Q(basket__icontains=keyword) |
                Q(uraian__icontains=keyword))

    contract_list = query.distinct().order_by('-id')

    return JsonResponse(contract_list)


