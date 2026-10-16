from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Organization,Membership,Course
@api_view(['GET'])
@permission_classes([AllowAny])
def health(request):
    return JsonResponse({'status':'ok'})
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def organizations(request):
    data=list(Organization.objects.filter(membership__user=request.user).values('id','name').distinct())
    return JsonResponse({'organizations':data})
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def courses(request,organization_id):
    if not Membership.objects.filter(organization_id=organization_id,user=request.user).exists():
        return JsonResponse({'detail':'Not found'},status=404)
    data=list(Course.objects.filter(organization_id=organization_id).values('id','title'))
    return JsonResponse({'courses':data})
