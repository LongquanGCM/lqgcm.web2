 #coding=utf-8 

from django.db import models
from django import forms
import django.utils.timezone as timezone
from ckeditor_uploader.fields import  RichTextUploadingField

#class Category(models.Model):
#    category_name = models.CharField('分类', max_length=256)
#    
#    def __unicode__(self):
#        return '%s' %(self.category_name)
#

class InspirationColumn(models.Model):
    column_name = models.CharField('栏目名称', max_length=256)
    
    def __unicode__(self):
        return '%s' %(self.column_name)

class Inspiration(models.Model):
    column   = models.ForeignKey(InspirationColumn, related_name='inspiration', verbose_name='栏目名称（必选）', default='', on_delete=models.CASCADE)
    topic    = models.CharField('标题（必填）', max_length=200, default='')
    text     = RichTextUploadingField(blank=True, null=True, verbose_name="内容（可选）")
    picture  = models.ImageField('图片（可选）', upload_to = 'inspirations/', blank=True, default='') 
    pub_time = models.DateTimeField('发布日期（可选）', blank=True, default = timezone.now)

    def __unicode__(self):
        return unicode(self.topic) 


class Column(models.Model):
    column_name = models.CharField('栏目名称', max_length=256)
    
    def __unicode__(self):
        return '%s' %(self.column_name)

class Tag(models.Model):
    tag_name = models.CharField('标签名', max_length=256)
    
    def __unicode__(self):
        return '%s' %(self.tag_name)

class Article(models.Model):
    article_column      = models.ForeignKey(Column, related_name='article', verbose_name='栏目名称（必选）', on_delete=models.CASCADE)
    article_title       = models.CharField('标题（必填）', max_length=1000)
    article_pubDate     = models.DateTimeField('发表时间（必填）', default = timezone.now)
    article_author      = models.CharField('作者（可选）', blank=True, max_length=200)
    article_photo       = models.ImageField('图片（可选）', upload_to = 'articles/', blank=True, default='')
    article_description = RichTextUploadingField(blank=True,null=True,verbose_name="内容简介（可选）")
    article_content     = RichTextUploadingField(blank=True,null=True,verbose_name="详细内容（可选）")
#    article_category    = models.ForeignKey(Category, related_name='article', on_delete=models.CASCADE)
    article_source      = models.CharField('信息来源（可选）', max_length=200, blank=True, default='') 
    article_tag         = models.ManyToManyField(Tag, blank=True, verbose_name='标签')
    article_click       = models.IntegerField('访问量', blank=True, null=True)
    article_top         = models.BooleanField('是否置顶', default=False)
    article_published   = models.BooleanField('正式发布', default=True) 
    
    def __unicode__(self):
        return '%s' %(self.article_title)

class Comment(models.Model):
    
    comment_name = models.CharField(max_length=256)
    comment_email = models.CharField(max_length=256)
    comment_content = models.TextField()
    comment_time = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    article = models.ForeignKey(Article, related_name='article_comment', on_delete=models.CASCADE)
    comment_comment = models.ForeignKey("Comment",related_name='comment',null=True,blank=True,on_delete=models.CASCADE)
    
    def __unicode__(self):
        return '%s' %(self.comment_name)

# activity start #    
class ActivityColumn(models.Model):
    column_name = models.CharField('栏目名称', max_length=256)
    
    def __unicode__(self):
        return '%s' %(self.column_name)

class Activity(models.Model):
    activity_column       = models.ForeignKey(ActivityColumn, related_name='activity', verbose_name='栏目名称（必选）', on_delete=models.CASCADE)
    activity_title        = models.CharField('标题（必填）', max_length=200, primary_key=True)
    activity_location     = models.CharField('地点（必填）', max_length=100, default='')
    activity_date         = models.DateTimeField('活动日期（必填）')
    activity_description  = models.TextField('内容简介（必填）', max_length=2000, default='')
    activity_content      = RichTextUploadingField(blank=True,null=True,verbose_name="详细内容（可选）")
    activity_photo        = models.ImageField('图片（可选）', upload_to = 'activities/', blank=True, default='') 
    activity_source       = models.CharField('信息来源（可选）', max_length=200, blank=True, default='') 
    activity_publisher    = models.CharField('发布者（可选）', max_length=100, blank=True, default='')
    activity_publish_time = models.DateTimeField('发布日期（可选）', blank=True, default = timezone.now)

    def __unicode__(self):
        return 'Activity:%s,Date:%s' %(self.activity_title,self.activity_publish_time)

class ActivitySchedule(models.Model):
    activity = models.ForeignKey(Activity, related_name='activity_schedule', on_delete=models.CASCADE);
    activity_schedule = models.CharField(max_length=200) 
    
    def __unicode__(self):
        return '%s' %(self.activity_schedule)
    
class ActivityEnroll(models.Model):
    activity = models.ForeignKey(Activity, related_name='activity_enroll', on_delete=models.CASCADE);
    name = models.CharField(max_length=40) 
    email = models.CharField(max_length=60) 
    lunch = models.CharField(max_length=10) 
    
    def __unicode__(self):
        return '%s' %(self.name)

class Speaker(models.Model):
    activity = models.ForeignKey(Activity, related_name='activity_speakers', default='', on_delete=models.CASCADE);
#    activity = models.ManyToManyField(Activity, related_name='speakers');
    name  = models.CharField('姓名（必填）', max_length=200, primary_key=True)
    role  = models.CharField('职位（必填）', max_length=100, default='')
    photo = models.ImageField('图片（必填）', upload_to = 'speakers/', blank=True, default='') 
    topic_title   = models.CharField('学术交流题目（必填）', max_length=100, default='')
    topic_desc    = models.TextField('演讲内容简介（必填）', max_length=2000, default='')
    topic_content = models.TextField('演讲完整内容（必填）', max_length=20000, default='')

    # when you want to for loop items in speaker list, below info "Name and Topic" will be returned.
    def __unicode__(self):
        return 'Name:%s,Topic:%s' %(self.name,self.topic_title)

# activity end #    

class Team(models.Model):
    team_member_name = models.CharField(max_length=40)
    team_member_title = models.CharField(max_length=100)
    team_member_photo = models.ImageField(upload_to = 'team/')
    team_member_profile = models.TextField()
 
 
class EmailSub(models.Model):
    email_address = models.CharField(max_length=60, primary_key=True)
    name = models.CharField(max_length=40)
    add_time = models.DateTimeField(default = timezone.now)

class Volunteer(models.Model):
    family_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    email = models.CharField(max_length=60)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    zip = models.CharField(max_length=10)
    telephone = models.CharField(max_length=20)
    mobilephone = models.CharField(max_length=20) 
    skills = models.CharField(max_length=300)
    contact_message = models.CharField(max_length=300)        
    add_time = models.DateTimeField(default = timezone.now)
    
    class Meta:  
        unique_together = ('family_name', 'first_name' ,'email')  
      
    primary = ('family_name', 'first_name' ,'email')  
      
    def __unicode__(self):  
        return '%s,%s,%s'%(self.family_name,self.first_name ,self.email)  