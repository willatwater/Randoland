from django.contrib import admin

from .models import Thinkpiece, BillBreakdown, BreakdownItem, Images, Roundup


# Register your models here.


 
@admin.register(BreakdownItem)
class BreadownItemAdmin(admin.ModelAdmin):
    list_display = ('billbreakdown', 'title')
    ordering = ('billbreakdown',)
    search_fields = ('title',)
    
 
    class Meta:
       model = BreakdownItem
 
    
class ThinkpieceAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','image','status','created_on')
    list_filter = ("status",)
    search_fields = ['title','content',]
    prepopulated_fields = {'slug':('title',)}
    
class RoundupAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','status','created_on')
    list_filter = ("status",)
    search_fields = ['title','content',]
    prepopulated_fields = {'slug':('title',)}
    

admin.site.register(Thinkpiece,ThinkpieceAdmin)
admin.site.register(BillBreakdown)
admin.site.register(Images)
admin.site.register(Roundup, RoundupAdmin)
