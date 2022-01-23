from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status

from rest_framework.response import Response

class BaseAPIView(viewsets.ViewSet):
    def get(self, request):
        if self.mandatory_params:
            for param in self.mandatory_params:
                return not request.GET.get(param)

# Remove this class or use it as template
class TestViewset(BaseAPIView):
    mandatory_params = (None)
    permission_classes = (permissions.AllowAny, )

    def list(self, request):
        if super().get(request):
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={'msg': 'Not all mandatory params were found.'}
            )

        return Response(status=status.HTTP_200_OK, 
                        data={'msg': 'It works!'})