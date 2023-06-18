from shortener.views import index, get_user
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index, name='index_1'),
    path("get_user/<int:user_id>",get_user),
    # http://127.0.0.1:8000/get_user/1?username=hello

]
