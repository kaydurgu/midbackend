from django.contrib import admin
from django.urls import path
from women.views import *
from rest_framework.schemas import get_schema_view
from .yasg import urlpatterns as doc_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_schema', get_schema_view(title='Famous Women API'), name='api-schema'),
    path("api/vi/womenlist/", WomenAPIList.as_view(), name="womenlist"),
    path('api/vi/womenlist_update_data/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/vi/womendetail/<int:pk>/', WomenAPIDetailView.as_view()),
    path('api/vi/catergorylist/', CaregoryAPIView.as_view()),
    path('api/vi/catergory_update_data/<int:pk>', CategoryAPIUpdate.as_view()),
]
urlpatterns+=doc_urls