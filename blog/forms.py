# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 15:13:06 2021

@author: Will
"""

from django import forms

from .models import Thinkpiece, BillBreakdown, BreakdownItem, Images, Roundup


class ThinkpieceForm(forms.ModelForm):
    
    class Meta:
        model = Thinkpiece
        fields = ['title','author','blurb','status','content','image',]
        labels = {
            'title':'Title',
            'author':'Author',
            'blurb':'Lede',
            'status':'Status',
            'content':'Text',
            }
        
class RoundupForm(forms.ModelForm):
    
    class Meta:
        model = Roundup
        fields = ['title','author','status','content',]
        labels = {
            'title':'Title',
            'author':'Author',
            'status':'Status',
            'content':'Roundup text',
            'image':'Image',
            }


                
        
class BillBreakdownForm(forms.ModelForm):
    class Meta:
        model = BillBreakdown
        fields = ['title','bill_link','blurb','status']
        labels = {
            'title':'Title',
            'bill_link':'Link to bill text',
            'blurb':'Lede',
            'status':'Status',
            }

class BreakdownItemForm(forms.ModelForm):
    class Meta:
        model = BreakdownItem
        fields = ['billbreakdown','title','text',]
        labels = {
            'billbreakdown':'Bill',
            'title':'Title',
            'text':'Comment',
            }
        
class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')    
    class Meta:
        model = Images
        fields = ('image', )
        labels = {'Image:'}
