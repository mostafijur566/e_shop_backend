from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import *
from .models import CustomerDetails as customerModel
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


class CustomerDetails(APIView):
    permission_classes = []

    def post(self, request):
        serializer = CustomerDetailsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Registration successfully!",
            }
            http_response = status.HTTP_200_OK

        else:
            data = {
                "message": serializer.errors
            }
            http_response = status.HTTP_400_BAD_REQUEST
        return Response(data, status=http_response)

    def get(self, request):
        customer = customerModel.objects.get(user=request.user)
        serializer = CustomerDetailsSerializers(customer, many=False)

        return Response(serializer.data)

    def put(self, request):
        customer = customerModel.objects.get(user=request.user)
        serializer = CustomerDetailsSerializers(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Updated successfully!"
            }
            http_response = status.HTTP_200_OK

        else:
            data = {
                "message": "Something went wrong"
            }
            http_response = status.HTTP_400_BAD_REQUEST

        return Response(data, status=http_response)


class ProductCategoriesView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ProductCategoriesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Added successfully!",
            }
            http_response = status.HTTP_200_OK

        else:
            data = {
                "message": serializer.errors
            }
            http_response = status.HTTP_400_BAD_REQUEST
        return Response(data, status=http_response)

    def get(self, request):
        category = ProductCategories.objects.all()
        serializer = ProductCategoriesSerializers(category, many=True)

        return Response(serializer.data)

    def put(self, request, pk):
        category = ProductCategories.objects.get(id=pk)
        serializer = ProductCategoriesSerializers(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Updated successfully!",
            }
            http_response = status.HTTP_200_OK

        else:
            data = {
                "message": serializer.errors
            }
            http_response = status.HTTP_400_BAD_REQUEST
        return Response(data, status=http_response)

    def delete(self, request, pk):
        category = ProductCategories.objects.get(id=pk)
        category.delete()
        return Response(
            {
                "message": "Deleted successfully!"
            }
        )


class ProductView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Added successfully!",
            }
            http_response = status.HTTP_200_OK

        else:
            data = {
                "message": serializer.errors
            }
            http_response = status.HTTP_400_BAD_REQUEST

        return Response(data, status=http_response)

    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializers(product, many=True)

        return Response(
            {
                "total_product": Product.objects.count(),
                "products": serializer.data
            }
        )

    def put(self, request, pk):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializers(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Updated successfully!",
            }
            http_response = status.HTTP_200_OK

        else:
            data = {
                "message": serializer.errors
            }
            http_response = status.HTTP_400_BAD_REQUEST
        return Response(data, status=http_response)

    def delete(self, request, pk):
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(
            {
                "message": "Deleted successfully!"
            }
        )

class SingleProductView(APIView):

    permission_classes = []

    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializers(product, many=False)
        return Response(serializer.data)

class OrderDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = OrderDetailsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Product added successfully!",
            }
            http_response = status.HTTP_200_OK

        else:
            data = {
                "message": serializer.errors
            }
            http_response = status.HTTP_400_BAD_REQUEST

        return Response(data, status=http_response)

    def get(self, request):
        order = OrderDetails.objects.all()
        serializer = OrderDetailsSerializers(order, many=True)

        return Response(
            {
                "total_order": Product.objects.count(),
                "order": serializer.data
            }
        )

    def put(self, request, pk):
        order = OrderDetails.objects.get(id=pk)
        serializer = OrderDetailsSerializers(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Updated successfully!",
            }
            http_response = status.HTTP_200_OK

        else:
            data = {
                "message": serializer.errors
            }
            http_response = status.HTTP_400_BAD_REQUEST
        return Response(data, status=http_response)

    def delete(self, request, pk):
        order = OrderDetails.objects.get(id=pk)
        order.delete()
        return Response(
            {
                "message": "Deleted successfully!"
            }
        )


class OrderView(APIView):
    def get(self, request):
        order = Order.objects.all()
        serializer = OrderSerializers(order, many=True)

        return Response(
            {
                "total_order": Product.objects.count(),
                "order": serializer.data
            }
        )

    def post(self, request):
        serializer = OrderSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Your order added successfully!",
            }
            http_response = status.HTTP_200_OK

        else:
            data = {
                "message": serializer.errors
            }
            http_response = status.HTTP_400_BAD_REQUEST

        return Response(data, status=http_response)


class OrderHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = OrderHistorySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Added to history",
            }
            http_response = status.HTTP_200_OK

        else:
            data = {
                "message": serializer.errors
            }
            http_response = status.HTTP_400_BAD_REQUEST

        return Response(data, status=http_response)

    def get(self, request):
        history = OrderHistory.objects.filter(user=request.user)
        serializer = OrderHistorySerializers(history, many=True)

        return Response(
            {
                "total_order": history.count(),
                "order": serializer.data
            }
        )

