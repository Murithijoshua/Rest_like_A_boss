# from reddit_clone.app.views import PostList
from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/all', views.PostList.as_view()),
    path('api/all/<int:pk>', views.PostRetrieveDestroy.as_view()),
    path('api/all/<int:pk>/vote', views.VoteCreate.as_view()),
    path('api/auth', include('rest_framework.urls')),

]
