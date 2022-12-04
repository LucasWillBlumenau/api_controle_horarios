from rest_framework.generics import ListAPIView
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .serializers import LogSerializer
from .models import Log


class LogViewSet(ListAPIView):

    queryset = Log.objects.all()
    serializer_class = LogSerializer
    permission_classes = (IsAdminUser, )
    authentication_classes = (BasicAuthentication, SessionAuthentication )

