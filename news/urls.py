from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
    url('^today/$',views.news_of_day,name = 'newsToday'),
    url('^$',views.welcome,name = 'welcome')
    
]