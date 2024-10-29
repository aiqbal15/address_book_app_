from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Address
from .serializers import AddressSerializer
from drf_spectacular.utils import extend_schema,extend_schema_view, OpenApiResponse

def find_address(id):
    try:
        return Address.objects.get(pk=id)        
    except Address.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@extend_schema(
        request=None,
        responses={
            200: OpenApiResponse(response=AddressSerializer(many=True), description="List of addresses"),
            500: OpenApiResponse(description="Internal Server Error")
        }
    )
@api_view(['GET'])
def get_addresses(request):
    try:
        address_list = Address.objects.all()
        serializer = AddressSerializer(address_list, many=True)
        return Response(serializer.data)
    
    except:
        return Response("Unable to get address list.",status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@extend_schema(
        request=AddressSerializer,
        responses={
            200: OpenApiResponse(response=AddressSerializer, description="The address added."),
            400: OpenApiResponse(description="Bad Request. This happens when the request has errors from the users side."),
            500: OpenApiResponse(description="Internal Server Error. This happens in case of a save failure.")
        }
    )
@api_view(['POST'])
def create_address(request):
    try:
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except:
        return Response("Unable to save address.", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@extend_schema_view(
    get=extend_schema(        
        responses={
            200: OpenApiResponse(response=AddressSerializer, description="The address with ID provided."),
            404: OpenApiResponse(description="Not found. If the ID fetched doesn't exist."),
            500: OpenApiResponse(description="Internal Server Error. This happens in case of a fetch failure.")
        }
    ),
    delete=extend_schema(
        responses={
            204: OpenApiResponse(description="Address {id} deleted successfully"),
            404: OpenApiResponse(description="Not found. If the ID to be deleted doesn't exist."),
            500: OpenApiResponse(description="Internal Server Error. System error in deleting.")
        }
    ),
    put=extend_schema(
        request=AddressSerializer,
        responses={
            200: OpenApiResponse(response=AddressSerializer, description="Successful PUT response."),
            400: OpenApiResponse(description="Bad Request. Cannot be added."),
            404: OpenApiResponse(description="Not found. If the ID to be updated doesn't exist."),
            500: OpenApiResponse(description="Internal Server Error. Unable to update address.")
        }
    )
)
@api_view(['GET', 'DELETE', 'PUT'])
def address_detail(request, id):    
    address = find_address(id)

    if request.method == 'GET':
        try:
            serializer = AddressSerializer(address)
            return Response(serializer.data, status=status.HTTP_200_OK)        
        except:
            return Response(data="Unable to fetch address.", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    elif request.method == 'DELETE':
        try:
            address.delete()
            return Response(data=f"Address {id} deleted successfully.", status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(data="Unable to delete address.", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    elif request.method == 'PUT':
        try:
            serializer = AddressSerializer(address, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        
        except:
            return Response(data="Unable to update address.", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    else:
        return Response("Unsupported Request.", status=status.HTTP_400_BAD_REQUEST)


