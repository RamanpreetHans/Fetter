from django.urls import path
from django.contrib import admin
from basicapp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'basicapp'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('instituteAdmin/adduser/', views.adduser, name='adduser'),
    path('accountInfo/', views.userAccountInfo, name='accountInfo'),
    path('addnewsfeed/', views.addNewsFeed, name='addnewsfeed'),
    path('index/', views.index, name='index'),
    path('InstituteProfilePage/', views.instituteprofilepage, name='InstituteProfilePage'),
    path('instituteAdmin/InstituteExtra/', views.InstituteExtra, name='InstituteInfo'),
    path('index/addNewsFeed/', views.instituteAdmin, name='newsfeed'),
    path('InstituteExtra/InstituteSocities/', views.institutesocities, name='InstituteSocities'),
    path('index/<int:pk>/', views.NewsFeedDetail.as_view(), name ='detail'),
    path('index/<int:pk>/comment/', views.add_comment_to_post, name = 'add_comment_to_post'),
    path('index/internships/', views.internships, name = 'internships'),
    path('index/scholarships/', views.scholarships, name = 'scholarships'),
    path('index/programmes/', views.programmes, name = 'programmes'),
    path('index/addUserInterest/', views.addUserInterest, name='addUserInterest'),
    

]

urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
