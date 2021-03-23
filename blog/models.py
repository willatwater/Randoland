from django.db import models

from ckeditor.fields import RichTextField

from django.contrib.auth.models import User

from django.db.models.signals import pre_save

from utils import unique_slug_generator

from django.utils.text import slugify


# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Publish")
    )



class BillBreakdown(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='billbreakdownauthor')
    blurb = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length = 100, null=True,blank=True)
    bill_link = models.URLField(max_length=200)
    updated_on = models.DateField(auto_now=True)
    created_on = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
       
    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title
    


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=BillBreakdown)


class BreakdownItem(models.Model):
    billbreakdown = models.ForeignKey(BillBreakdown,verbose_name="Bill", 
                                      on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'breakdown items'
        ordering = ['created_on']
    
    def __str__(self):
        """Return string representation of model"""
        return self.title

class Images(models.Model):
    breakdownitem = models.ForeignKey(BreakdownItem, default=None, 
                                      on_delete=models.CASCADE)
    
    image = models.ImageField(upload_to='images',
                              verbose_name='Image',blank=True)
    
    
     
    class Meta:
        verbose_name_plural = 'Images'
    
    def __str__(self):
        return self.breakdownitem.title


    
class Thinkpiece(models.Model):
    title = models.CharField(max_length=200)
    blurb = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='thinkpieces')
    updated_on = models.DateField(auto_now=True)
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/thinkpieces',
                              verbose_name='Image',blank=True)
    created_on = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    
    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title


pre_save.connect(slug_generator, sender=Thinkpiece)


class Roundup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='roundups')
    content = RichTextField(blank=True, null=True)
    created_on = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    
    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title

pre_save.connect(slug_generator, sender=Roundup)