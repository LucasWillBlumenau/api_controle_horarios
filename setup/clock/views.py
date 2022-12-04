from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .models import Clock
from .serializers import ClockSerializer, PunchInfoSerializer


class ClockViewSet(APIView):

    serializer_class = ClockSerializer
    authentication_classes = (BasicAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        try:
            clock = Clock(user=request.user, punch_type=request.data['punch_type'])
            clock.save()
            return Response({'status': 'ponto batido com sucesso'})
        except Exception as e:
            return Response(status=500)
            
        

class PunchInfoView(ListAPIView):

    queryset = Clock.objects.all()
    serializer_class = PunchInfoSerializer
    authentication_classes = (BasicAuthentication, SessionAuthentication)
    permission_classes = (IsAdminUser, )