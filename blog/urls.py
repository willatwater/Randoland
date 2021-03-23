# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 20:21:29 2021

@author: Will
"""
from . import views

from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('',views.index, name='home'),
    # View thinkpieces
    path('thinkpieces/', views.ThinkpieceList.as_view(), name='thinkpieces'),
    path('thinkpieces/<slug:slug>/', views.ThinkpieceDetail.as_view(), 
         name='thinkpiece_detail'),
    # View Breakdowns
    path('bill_breakdowns/', views.bill_breakdowns, name='bill_breakdowns'),
    path('bill_breakdowns/<slug:slug_text>/',views.bill_breakdown,
         name='bill_breakdown'),
    path('bill_breakdowns/<slug:slug_text>/<int:pic_id>/',
         views.pics,name='pics'),
      
    # Roundup
    path('roundups/',views.RoundupList.as_view(),name='roundups'),
    path('roundups/<slug:slug>/', views.RoundupDetail.as_view(), 
         name='roundup_detail'),
      
    # Backend
    path('admin_main/', views.admin_main, name='admin_main'),
    
    # Thinkpieces
    path('new_thinkpiece/', views.new_thinkpiece, name='new_thinkpiece'),
    path('thinkpieces/<slug:slug>/edit', views.edit_thinkpiece, 
         name='edit_thinkpiece'),
    path('thinkpieces/<slug:slug>/delete', views.delete_thinkpiece, 
         name='delete_thinkpiece'),
    
    
    # Roundups
    path('new_roundup/', views.new_roundup, name='new_roundup'),
    path('roundup/<slug:slug>/edit', views.edit_roundup, 
         name='edit_roundup'),
    path('roundup/<slug:slug>/delete', views.delete_roundup, 
         name='delete_roundup'),
    
    # Bill Breakdowns
    path('new_bill_breakdown/', views.new_bill_breakdown, 
         name='new_bill_breakdown'),
    path('edit/bill_breakdowns/<slug:slug_text>', views.edit_breakdown_view,
         name='edit_breakdown_view'),
    path('new_detail/bill_breakdowns/<slug:slug_text>/', 
         views.new_breakdown_detail, name='new_breakdown_detail'),
    path('edit/bill_breakdowns/<slug:slug_text>/', views.edit_breakdown_head,
         name='edit_breakdown_head'),
    path('edit/bill_breakdowns/<slug:slug_text>/<int:breakdownitem_id>/', 
         views.edit_breakdown_detail,name='edit_breakdown_detail'),
    path('delete/bill_breakdowns/<slug:slug_text>/', views.delete_breakdown, 
         name='delete_breakdown'),
    path('delete/bill_breakdowns/<slug:slug_text>/<int:breakdownitem_id>/', 
         views.delete_breakdown_detail, name='delete_breakdown_item'),
    
    ]