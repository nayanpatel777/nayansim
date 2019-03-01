
from django.conf.urls import url
#from django.urls import path
from nayan import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
#    url(r'host/', views.hostpage.as_view(),name='host'),
#    url(r'install/', views.installpage.as_view(),name='install'),    

    url('c_hostname/ ', views.my_view1,name='my_view_name1'),
    url('p_packageinstall/ ', views.my_view2,name='my_view_name2')

]

