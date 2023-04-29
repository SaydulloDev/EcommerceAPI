from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializers


# Create your views here.

@api_view(['GET'])
def get_users_list(request):
    users = User.objects.order_by('-id')
    serializer = UserSerializers(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    serializer = UserSerializers(user, many=False)
    return Response(serializer.data)
