from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth.models import User
from .models import Job, Collaborator
from .serializers import JobSerializer, CollaboratorSerializer, UserSerializer
from logs.models import Log


class CollaboratorViewSet(CreateAPIView):

    serializer_class = CollaboratorSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAdminUser, )

class JobViewSet(CreateAPIView):

    queryset = Job.objects.all()
    serializer_class = JobSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAdminUser, )


class UserViewSet(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAdminUser, )


class CollaboratorDetails(APIView):

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )

    def get(self, request, id):  
        try:
            collaborator_details = Collaborator.objects.get(id=id)
        except Collaborator.DoesNotExist:
            return Response(status=404)
        except Exception as e:
            print(e)
            return Response(status=500)

        serializer = CollaboratorSerializer(collaborator_details)
        return Response(serializer.data)
    
    def delete(self, request, id):
        
        try:
            collaborator = Collaborator.objects.get(id=id)
            log = Log(log_type=2, user=request.user, collaborator=[collaborator.firstname, collaborator.cpf])
            User.objects.get(id=collaborator.user.id).delete()
            collaborator.delete()
            log.save()
        except Exception:
            return Response(status=500)
        return Response({'status': 'collaborator deleted sucesfully'})