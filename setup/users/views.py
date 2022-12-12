from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth.models import User
from .models import Job, Collaborator
from .serializers import JobSerializer, CollaboratorSerializer, UserSerializer
from logs.models import Log


class CollaboratorViewSet(APIView):

    serializer_class = CollaboratorSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAdminUser, )

    def post(self, request):
        serializer = CollaboratorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            log = Log(
                log_type=0, 
                    user=request.user, 
                    collaborator=[serializer.data['firstname'], 
                    serializer.data['cpf']]
                )
            log.save()
            return Response(status=201)
        return Response(status=401)


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


class CollaboratorsDetails(ListAPIView):

    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAdminUser, )
    

class CollaboratorDetails(APIView):

    serializer_class = CollaboratorSerializer
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

    def put(self, request, id):
        try:
            collaborator = Collaborator.objects.get(id=id)
            serializer = CollaboratorSerializer(collaborator, data=request.data)
        except Collaborator.DoesNotExits:
            return Response(status=404)
        if not serializer.is_valid():
            return Response(status=400)
        serializer.save()
        log = Log(log_type=1, user=request.user, collaborator=[collaborator.firstname, collaborator.cpf])
        log.save()
        return Response(serializer.data, status=200)
