from django.conf.urls import url, include
from . import views
from stockplot.models import Twse

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    #url(r'^(?P<codeid>[a-zA-Z0-9]{4,})', views.byCode, name='byCode'),
]
