from .models import userInfo
from .serializers import userInfoSerializer
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser


# Create your views here.
@api_view(['GET'])
def user_info_list(request, name=None, phone=None):
    """
        사용자 정보 데이터 조회 함수
        @param name  사용자 이름
        @param phone  사용자 연락처

        변수가 없을 경우 모든 데이터 조회
        name 변수가 있을 경우 성함이 name인 모든 사용자 데이터 조회
        phone 변수가 있을 경우 해당 연락처의 데이터 조회
    """
    params = {}
    if name:
        params['name'] = name

    if phone:
        params['phoneNo'] = phone

    if not params:
        query_set = userInfo.objects.all()
    else:
        query_set = userInfo.objects.filter(**params)

    serializer = userInfoSerializer(query_set, many=True)
    return JsonResponse(serializer.data, json_dumps_params={'ensure_ascii': False}, safe=False, status=200)


@api_view(['POST'])
def insert_user_info(request):
    """
        사용자 정보 추가 함수

        설명 :
            전달 받은 변수들을 유효성 체크 후
                문제 있으면 201 return
                문제 없을 경우 DB에 해당 데이터 저장
    """

    data = request.data
    serializer = userInfoSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, json_dumps_params={'ensure_ascii': False}, status=201)
    return JsonResponse(serializer.errors, json_dumps_params={'ensure_ascii': False}, status=400)


@api_view(['PUT', 'DELETE'])
def user_info_detail(request, id=None):
    """
        사용자 정보 수정/삭제 함수

        @param id  사용자정보에 레코드 아이디

        수정/삭제 할 데이터 조회
            조회한 데이터가 없을 경우 404 return
            데이터가 존재할 경우 수정/삭제 진행

        PUT (수정) :
            name, age, phoneNo, address, email 변수들을 유효성 체크 후 문제 없을 경우 DB에서 해당 데이터 수정

        DELETE (삭제) :
            해당 데이터 삭제
    """

    try:
        query_set = userInfo.objects.get(id=id)
    except userInfoSerializer.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = userInfoSerializer(query_set, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, json_dumps_params={'ensure_ascii': False})
        return JsonResponse(serializer.errors, json_dumps_params={'ensure_ascii': False}, status=400)

    elif request.method == 'DELETE':
        query_set.delete()
        return HttpResponse(status=204)
