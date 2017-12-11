from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ServiciosExternosSerializer
from .models import ServiciosExternos
from django.http import Http404


class ListServiciosExternos(APIView):

    def get(self, request):
        servicios = ServiciosExternos.objects.all()
        servicio_json = ServiciosExternosSerializer(servicios, many=True)
        return Response(servicio_json.data)

    def post(self, request):
        servicio_json = ServiciosExternosSerializer(data=request.data)
        if servicio_json.is_valid():
            servicio_json.save()
            return Response(servicio_json.data, status=201)
        return Response(servicio_json.errors, status=400)


class DetailServiciosExternos(APIView):

    def get_object(self, pk):
        try:
            return ServiciosExternos.objects.get(id=pk)
        except ServiciosExternos.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        servicio = self.get_object(pk)
        servicio_json = ServiciosExternosSerializer(servicio)
        return Response(servicio_json.data)

    def put(self, request, pk):
        servicio = self.get_object(pk)
        servicio_json = ServiciosExternosSerializer(servicio,
                                                    data=request.data)
        if servicio_json.is_valid():
            servicio_json.is_valid()
            return Response(servicio_json.data)
        return Response(servicio_json, status=400)

    def delete(self, request, pk):
        servicio = self.get_object(pk)
        servicio.delete()
        return Response(status=204)
