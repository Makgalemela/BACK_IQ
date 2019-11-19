from AssetMgmt.models import Screen
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response

class DeviceListView(generics.ListAPIView):
    queryset = Screen.objects.all()
    serializer_class = serializers.ScreenSerializer


class DeviceCreateView(generics.CreateAPIView):
    queryset = Screen.objects.all()
    serializer_class = serializers.ScreenSerializer

    def create(self, request, *args, **kwargs):
        super(DeviceCreateView, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created",
                    "result": request.data}
        return Response(response)

class DeviceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Screen.objects.all()
    serializer_class = serializers.ScreenSerializer

    def patch(self, request, *args, **kwargs):
        super(DeviceDetailView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully updated",
                    "result": data}
        return Response(response)

    # def delete(self, request, *args, **kwargs):
    #     super(DeviceDetailView, self).delete(request, args, kwargs)
    #     response = {"status_code": status.HTTP_200_OK,
    #                 "message": "Successfully deleted"}
    #     return Response(response)

    # def retrieve(self, request, *args, **kwargs):
    #     super(DeviceDetailView, self).retrieve(request, args, kwargs)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     data = serializer.data
    #     response = {"status_code": status.HTTP_200_OK,
    #                 "message": "Successfully retrieved",
    #                 "result": data}
    #     return Response(response)

   

      
