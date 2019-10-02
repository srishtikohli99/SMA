# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 07:32:53 2019

@author: srishti
"""

from django.conf.urls import url
from firstapp import views
from django.urls import path
from . import views


app_name = 'firstapp'

urlpatterns = [
        # url(r'^$',views.index,name='index'),
        #url(r'^firstapp/',include('firstapp.urls')),
       # ex: /polls/5/
       path('',views.index),
       #path('feed/',views.tail),
        path('fire/<key>/',views.fire),
        path('load/loadyes/',views.loady),
        path('load/loadno/',views.loadn),
       path('thanks/', views.thanks),
    path('<int:question_id>/', views.detail),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote),
    
   
]