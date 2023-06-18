from django.shortcuts import render,redirect
from shortener.models import Users
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

def index(request):
    user = Users.objects.filter(username='admin').first() 
    # users 테이블에서 username 이 amdin인 것을 필터해서 첫번째 것을 가져와라 없으면 None이 반환됨
    email = user.email if user else "Anonymous User!"
    print(email)
    # user가 로그인 이되어있는지 확인
    # print(request.user.is_authenticated)
    # if request.user.is_authenticated is False:
    #     email = "Anonymous User!"
    #     print(email)
    return render(request, "base.html", {"welcome_msg": "Hello FastCampus!", "hello": "world!"})


@csrf_exempt    # 장고는 처음 페이지를 렌더링할때 csrf 토큰을 페이지에 발급함 , 이 토큰을 가지고 vaild한 요청인지 판단함 _exempt는 이를 면제하라는 의미  
def get_user(request, user_id): # user_id : 패스 파라미터 -> url.py에서 넘겨줌 
    print(user_id)
    # 브라우저에서는 get메소드만 가능한 상태임
    if request.method == "GET":
        abc = request.GET.get("abc") # 쿼리스트링으로 데이터를 백엔드로 보낼 수 있다.
        xyz = request.GET.get("xyz")    # http://127.0.0.1:8000/get_user/1?abc=123&xyz=098 
        user = Users.objects.filter(pk=user_id).first()
        return render(request,"base.html",{"user": user, "params":[abc,xyz]})
    # Postman에서 POST메소드 
    elif request.method =="POST":
        username = request.GET.get("username")  # Post로 request하면 username을 
    if username:        
        user = Users.objects.filter(pk=user_id).update(username=username)   # 변경한다
    return JsonResponse(status=201 , data=dict(msg="포스트") ,safe=False)