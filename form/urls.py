from django.contrib import admin
from django.urls import path
from app.views import my_view, success_page

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", my_view, name="my_view"),
    path("success_page/", success_page, name="success_page"),
]
