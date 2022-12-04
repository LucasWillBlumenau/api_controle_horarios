from django.contrib import admin
from django.urls import path, include
from users.views import JobViewSet, CollaboratorViewSet, CollaboratorDetails, UserViewSet
from clock.views import ClockViewSet, PunchInfoView
from logs.views import LogViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auht/', include('rest_framework.urls')),
    path('api/punch-the-clock/', ClockViewSet.as_view()),
    path('api/punch-info/', PunchInfoView.as_view()),
    path('api/register-job/', JobViewSet.as_view()),
    path('api/register-collaborator/', CollaboratorViewSet.as_view()),
    path('api/collaborator-detail/<int:id>/', CollaboratorDetails.as_view()),
    path('api/collaborator-detail/', CollaboratorDetails.as_view()),
    path('api/register-user/', UserViewSet.as_view()),
    path('api/logs', LogViewSet.as_view())
]
