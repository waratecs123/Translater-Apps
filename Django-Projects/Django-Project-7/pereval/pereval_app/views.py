from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Pereval
from .serializers import PerevalSerializer


class SubmitDataView(APIView):
    def post(self, request):
        serializer = PerevalSerializer(data=request.data)
        if serializer.is_valid():
            try:
                pereval = serializer.save()
                return Response({
                    'status': status.HTTP_200_OK,
                    'message': None,
                    'id': pereval.id
                })
            except Exception as e:
                return Response({
                    'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                    'message': str(e),
                    'id': None
                }, status=500)

        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': serializer.errors,
            'id': None
        }, status=400)

    def get(self, request, pk=None):
        if pk:
            pereval = get_object_or_404(Pereval, pk=pk)
            serializer = PerevalSerializer(pereval)
            return Response(serializer.data)
        else:
            user_email = request.query_params.get('user__email', None)
            if user_email:
                perevals = Pereval.objects.filter(user__email=user_email)
                serializer = PerevalSerializer(perevals, many=True)
                return Response(serializer.data)
            return Response({"error": "Email parameter is required"}, status=400)

    def patch(self, request, pk):
        pereval = get_object_or_404(Pereval, pk=pk)

        if pereval.status != 'new':
            return Response({
                'state': 0,
                'message': 'Запись нельзя редактировать, так как она не в статусе "new"'
            }, status=400)

        data = request.data.copy()
        if 'user' in data:
            user_data = data['user']
            if 'email' in user_data:
                del user_data['email']
            if 'phone' in user_data:
                del user_data['phone']
            if 'last_name' in user_data:
                del user_data['last_name']
            if 'first_name' in user_data:
                del user_data['first_name']
            if 'patronymic' in user_data:
                del user_data['patronymic']

        serializer = PerevalSerializer(pereval, data=data, partial=True)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({
                    'state': 1,
                    'message': 'Запись успешно обновлена'
                })
            except Exception as e:
                return Response({
                    'state': 0,
                    'message': str(e)
                }, status=500)

        return Response({
            'state': 0,
            'message': serializer.errors
        }, status=400)