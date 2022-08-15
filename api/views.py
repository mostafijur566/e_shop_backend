from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import *
from rest_framework.authtoken.models import Token


# Create your views here.


class GetStatusView(APIView):
    permission_classes = []

    def get(self, request):
        return Response({
            "status": 200,
            "message": "yes! django is working!"
        })


class RegistrationView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = RegistrationSerializers(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['message'] = "Successfully registered"
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token
            http_response = status.HTTP_200_OK

        else:
            data = {
                "status": 400,
                "message": "something went wrong",
                "data": serializer.errors
            }
            http_response = status.HTTP_400_BAD_REQUEST

        return Response(data, status=http_response)

