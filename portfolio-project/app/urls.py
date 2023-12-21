from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home, name="home"),
    path("todolist", views.todolist, name="todo"),
] + static(settings.PROJECT_URL, document_root=settings.PROJECT_ROOT)