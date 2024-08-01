from django.contrib import admin
from django.urls import path

from ninja import NinjaAPI

api_v1 = NinjaAPI()
api_v1.add_router(prefix='accounts', router=)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', api_v1.urls),
]
