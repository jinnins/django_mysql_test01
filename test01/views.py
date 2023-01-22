from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Test01
from .serializers import TestDataSerializer


@api_view(['GET'])
def getTestDatas(request):
    datas = Test01.objects.all()
    serializer = TestDataSerializer(datas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTestData(request, name):
    data = Test01.objects.get(name=name)
    serializer = TestDataSerializer(data, many=False)
    return Response(serializer.data)