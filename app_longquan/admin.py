from django.contrib import admin
from django import forms
from django.db.models import Count

# Register your models here.
from .models import Column, Tag, Article, Comment, EmailSub, Volunteer, Team, Activity, ActivitySchedule, ActivityEnroll, ActivityColumn, Speaker, Inspiration, InspirationColumn
#Category, 

#class CategoryAdmin(admin.ModelAdmin):
#    list_display = ('category_name',)
   
class InspirationColumnAdmin(admin.ModelAdmin):
    list_display = ('column_name',)

class InspirationAdmin(admin.ModelAdmin):
    list_display = ('topic', 'text', 'picture', 'pub_time')
    
class ArticleColumnAdmin(admin.ModelAdmin):
    list_display = ('column_name',)

class ActivityColumnAdmin(admin.ModelAdmin):
    list_display = ('column_name',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name',)

class ArticleAdmin(admin.ModelAdmin):
    def article_tag(self, article):
        tags = []
        for tag in article.tags.all():
            tags.append(tag.tag_name)
        return ' '.join(tags)
    article_tag.short_description = 'article_tag'
        
    def get_queryset(self, request):
            return Article.objects.annotate(comment_count=Count('article_comment'))
        
    def comment_count(self, obj):
            return obj.comment_count
    comment_count.short_description = ('comment count')
    
    list_display = ('article_title','article_pubDate','article_author','article_description','article_column','article_tag','article_click','article_top','article_published') # 'article_category',
    

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_name','comment_email','comment_content','comment_time' , 'article','comment_comment')
    
class TeamAdmin(admin.ModelAdmin):
        list_display = ('team_member_name', 'team_member_title','team_member_photo','team_member_profile')
    
class ActivityScheduleAdminInline(admin.TabularInline):
    model = ActivitySchedule
        
class ActivitySpeakerAdminInline(admin.TabularInline):
    model = Speaker
        
class ActivityAdmin(admin.ModelAdmin):
    inlines = (ActivityScheduleAdminInline, ActivitySpeakerAdminInline, )
    list_display = ('activity_title', 'activity_column', 'activity_date', 'activity_description', 'enroll_count')
    
    def get_queryset(self, request):
            return Activity.objects.annotate(enroll_count=Count('activity_enroll'))
    def enroll_count(self, obj):
            return obj.enroll_count

    enroll_count.short_description = ('enroll count')

class ActivityEnrollAdmin(admin.ModelAdmin):
    list_display = ('activity', 'name', 'email', 'lunch')


class EmailSubAdmin(admin.ModelAdmin):
    list_display = ('email_address', 'name', 'add_time')

class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('family_name', 'first_name', 'email','address1', 'address2', 'city','country', 'zip', 'telephone','mobilephone', 'skills', 'contact_message', 'add_time')

#admin.site.register(Category, CategoryAdmin)
admin.site.register(InspirationColumn, InspirationColumnAdmin)
admin.site.register(Inspiration, InspirationAdmin)
admin.site.register(Column, ArticleColumnAdmin)
admin.site.register(ActivityColumn, ActivityColumnAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(EmailSub, EmailSubAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(ActivityEnroll, ActivityEnrollAdmin)
admin.site.register(Team, TeamAdmin)
