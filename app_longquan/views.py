 #coding=utf-8 

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic.base import TemplateView
from django.db import models
from django.core.mail import send_mail
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from smtplib import SMTPAuthenticationError
import datetime
import calendar
import json
from django.forms.models import model_to_dict
from django.core import serializers

#to enable encoding utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from models import Article, Column,Comment, EmailSub ,Volunteer, Activity, ActivityColumn, ActivityEnroll, Speaker, Inspiration, InspirationColumn
from forms import CommentForm
from django.template.context_processors import request
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from serializers import UserSerializer, GroupSerializer, EventSerializer, SeminarSerializer
import django.utils.timezone as timezone

ITEMS_PER_PAGE = 1

class UserViewSet(viewsets.ModelViewSet):
    """
    API端：允许查看和编辑用户
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API端：允许查看和编辑组
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class IndexView(generic.ListView):
    template_name = 'longquan/index.html'
    def get_queryset(self):
        return Activity.objects.all()

    

class HomePageView(TemplateView):
    template_name = "home.html"

def FayuView(request):
    try:
        model = Inspiration.objects.filter(column=InspirationColumn.objects.get(column_name='法语'));
        return render(request, 'venerable-fayu.html',{
            'result_code':1, #查到结果，标识位为1
            'fayu_list': model
        })
    except ObjectDoesNotExist:
        return render(request, 'venerable-fayu.html', {
                     'result_code':0, #未查到结果，标识位为0
                 })

def FayuSingleView(request, fayu_topic):
    if(fayu_topic=='graphics.php'):
        return render(request, 'venerable-fayu-single.html', {
                     'result_code':0, #未查到结果，标识位为0
                 })
    else:
            try:
                 model = Inspiration.objects.get(topic=fayu_topic);
                 return render(request, 'venerable-fayu-single.html', {
                     'fayu': model
                 })
            except ObjectDoesNotExist:
                 return render(request, 'venerable-fayu-single.html', {
                     'result_code':0, #未查到结果，标识位为0
                 })

def DayiView(request):
    try:
        model = Inspiration.objects.filter(column=InspirationColumn.objects.get(column_name='大和尚答疑'));
        return render(request, 'venerable-dayi.html',{
            'result_code':1, #查到结果，标识位为1
            'dayi_list': model
        })
    except ObjectDoesNotExist:
        return render(request, 'venerable-dayi.html', {
                     'result_code':0, #未查到结果，标识位为0
                 })

def DayiSingleView(request, dayi_topic):
    if(dayi_topic=='graphics.php'):
        return render(request, 'venerable-dayi-single.html', {
                     'result_code':0, #未查到结果，标识位为0
                 })
    else:
            try:
                 model = Inspiration.objects.get(topic=dayi_topic);
                 return render(request, 'venerable-dayi-single.html', {
                     'dayi': model
                 })
            except ObjectDoesNotExist:
                 return render(request, 'venerable-dayi-single.html', {
                     'result_code':0, #未查到结果，标识位为0
                 })

def XianerView(request):
    try:
        model = Inspiration.objects.filter(column=InspirationColumn.objects.get(column_name='小和尚贤二'));
        return render(request, 'xianer.html',{
            'result_code':1, #查到结果，标识位为1
            'xianer_list': model
        })
    except ObjectDoesNotExist:
        return render(request, 'xianer.html', {
                     'result_code':0, #未查到结果，标识位为0
                 })

def XianerSingleView(request, xianer_topic):
    if(xianer_topic=='graphics.php'):
        return render(request, 'xianer-single.html', {
                     'result_code':0, #未查到结果，标识位为0
                 })
    else:
            try:
                 model = Inspiration.objects.get(topic=xianer_topic);
                 return render(request, 'xianer-single.html', {
                     'xianer': model
                 })
            except ObjectDoesNotExist:
                 return render(request, 'xianer-single.html', {
                     'result_code':0, #未查到结果，标识位为0
                 })

class VenerableProfileView(TemplateView):
    template_name = 'venerable-profile.html'

class VenerableBlogView(generic.ListView):
    model = Article
    template_name = 'venerable-blog.html'
    paginate_by = ITEMS_PER_PAGE#一个页面显示的条目
    queryset = Article.objects.filter(article_column=Column.objects.get(column_name='著作'))

class VenerableSingleBlogDisplay(generic.DetailView):
    model = Article
    template_name = 'venerable-single-blog.html'
    
    def get_context_data(self, **kwargs):
        context = super(VenerableSingleBlogDisplay, self).get_context_data(**kwargs)
        context['commnets'] = Comment.objects.filter(article=self.object)
        context['form'] = CommentForm
        return context

class CommentFormView(generic.detail.SingleObjectMixin, generic.FormView):
    template_name = 'venerable-single-blog.html'
    form_class = CommentForm
    model = Article

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        return super(CommentFormView, self).post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('app_longquan:venerable-single-blog', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        """
         If the form is valid, redirect to the supplied URL
         """
        model_instance = form.save(commit=False)
        model_instance.article = self.object
        model_instance.comment_time = timezone.now
        model_instance.save()
        return HttpResponseRedirect(self.get_success_url())
    
class VenerableSingleBlogView(generic.View):
        
    def get(self, request, *args, **kwargs):
        view = VenerableSingleBlogDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentFormView.as_view()
        return view(request, *args, **kwargs)
    
        
def DabeishiyeView(request):
    try:
        model = Article.objects.filter(article_column=Column.objects.get(column_name='大悲视野'));
        return render(request, 'dabeishiye.html',{
            'result_code':1, #查到结果，标识位为1
            'dabeishiye_list': model
        })
    except ObjectDoesNotExist:
        return render(request, 'dabeishiye.html', {
                     'result_code':0, #未查到结果，标识位为0
                 })

def DabeishiyeSingleView(request,dabeishiye_title):
    if(dabeishiye_title=='graphics.php'):
        return render(request, 'dabeishiye-single.html', {
                     'result_code':0, #未查到结果，标识位为0
                 })
    else:
            try:
                 model = Article.objects.get(article_title=dabeishiye_title);
                 return render(request, 'dabeishiye-single.html', {
                     'dabeishiye': model
                 })
            except ObjectDoesNotExist:
                 return render(request, 'dabeishiye-single.html', {
                     'result_code':0, #未查到结果，标识位为0
                 })

def ReportView(request):
    try:
        model = Article.objects.filter(article_column=Column.objects.get(column_name='心得分享'));
        return render(request, 'report.html',{
            'result_code':1, #查到结果，标识位为1
            'report_list': model
        })
    except ObjectDoesNotExist:
        return render(request, 'report.html', {
                     'result_code':0, #未查到结果，标识位为0
                 })

def ReportSingleView(request, report_title):
    if(report_title=='graphics.php'):
        return render(request, 'report-single.html', {
                     'result_code':0, #未查到结果，标识位为0
                 })
    else:
            try:
                 model = Article.objects.get(article_title=report_title);
                 return render(request, 'report-single.html', {
                     'report': model
                 })
            except ObjectDoesNotExist:
                 return render(request, 'report-single.html', {
                     'result_code':0, #未查到结果，标识位为0
                 })

def RecordShareView(request):
    try:
        model = Article.objects.filter(article_column=Column.objects.get(column_name='活动心得'));
        return render(request, 'records-share.html',{
            'result_code':1, #查到结果，标识位为1
            'records_share_list': model
        })
    except ObjectDoesNotExist:
        return render(request, 'records-share.html', {
                     'result_code':0, #未查到结果，标识位为0
                 })

def RecordShareSingleView(request,recordshare_title):
    if(recordshare_title=='graphics.php'):
        return render(request, 'records-share-single.html', {
                     'result_code':0, #未查到结果，标识位为0
                 })
    else:
            try:
                 model = Article.objects.get(article_title=recordshare_title);
                 return render(request, 'records-share-single.html', {
                     'records_share': model
                 })
            except ObjectDoesNotExist:
                 return render(request, 'records-share-single.html', {
                     'result_code':0, #未查到结果，标识位为0
                 })

def ShareViewsView(request):
    try:
        model = Article.objects.filter(article_column=Column.objects.get(column_name='欧洲参访心得'));
        return render(request, 'share-views.html',{
            'result_code':1, #查到结果，标识位为1
            'share_views_list': model
        })
    except ObjectDoesNotExist:
        return render(request, 'share-views.html', {
                     'result_code':0, #未查到结果，标识位为0
                 })

def ShareViewsSingleView(request,shareviews_title):
    if(shareviews_title=='graphics.php'):
        return render(request, 'share-views-single.html', {
                     'result_code':0, #未查到结果，标识位为0
                 })
    else:
            try:
                 model = Article.objects.get(article_title=shareviews_title);
                 return render(request, 'share-views-single.html', {
                     'share_views': model
                 })
            except ObjectDoesNotExist:
                 return render(request, 'share-views-single.html', {
                     'result_code':0, #未查到结果，标识位为0
                 })




class AboutView(TemplateView):
    template_name = 'about.html'
    
class TeamView(TemplateView):
    template_name = 'team.html'
    
class GetInvolvedView(TemplateView):
    template_name = 'get-involved.html'
    
class ContactView(TemplateView):
    template_name = 'contact.html'

                 

def EventView(request):
    year = datetime.date.today().year
    month = datetime.date.today().month
    firstDayWeekDay, monthRange = calendar.monthrange(year, month)
    firstDay = datetime.date(year=year, month=month, day=1)
    lastDay = datetime.date(year=year, month=month, day=monthRange)
    try:
        model = Activity.objects.filter(activity_date__range=(firstDay,lastDay), activity_column=ActivityColumn.objects.get(column_name='法事活动'));
        serializer = EventSerializer(model, many=True)
        return render(request, 'events.html', {
            'result_code':1, #查到结果，标识位为1
            'event_list':  json.dumps(serializer.data),
            'firstDayWeekDay':firstDayWeekDay,
            'year':year,
            'month': month,
            'monthrange':monthRange,
        })
    except ObjectDoesNotExist:
        return render(request, 'events.html', {
            'result_code':0, #未查到结果，标识位为0
            'firstDayWeekDay':firstDayWeekDay,
            'year':year,
            'month': month,
            'monthrange':monthRange,
             })

    
def EventsSingleView(request,event_title,event_publish_time):
    if(event_publish_time=='graphics.php'):
        return render(request, 'events-single.html', {
                     'result_code':0, #未查到结果，标识位为0
                 })
    else:
            try:
                 model = Activity.objects.get(activity_title=event_title,activity_publish_time= event_publish_time)
                 serializer = EventSerializer(model, many=False)
                 return render(request, 'events-single.html',serializer.data)
            except ObjectDoesNotExist:
                 return render(request, 'events-single.html', {
                     'result_code':0, #未查到结果，标识位为0
                 })
                 
def UpcomingEventView(request):
    try:
        model =   Activity.objects.filter(activity_date__gt=datetime.date.today()).order_by('activity_date').first()
        serializer = EventSerializer(model, many=False)
        return JsonResponse(serializer.data,status=201) 
    except ObjectDoesNotExist:
        return render(request, 'sidebar_upcoming_events.html', {'result_code':0, #未查到结果，标识位为0
                                                      })            

def EventsEnrollView(request):
    if request.method == 'POST':
        event_title = request.POST.get('event_title')
        event_publish_time = request.POST.get('event_publish_time')
        name = request.POST.get('name')
        email = request.POST.get('email')
        lunch = request.POST.get('lunch')
        try:    
            event = Event.objects.get(event_title=event_title,event_publish_time= event_publish_time);
            EventEnroll.objects.create(event=event,name=name,email=email,lunch=lunch)
        except IntegrityError:
            return HttpResponse('您已经报名参见，请勿重复报名！')
        return HttpResponse('报名成功，欢迎报名参加！')
     
    else:
        return HttpResponse('报名失败')
    

def SeminarView(request):
    try:
        model = Activity.objects.filter(activity_column=ActivityColumn.objects.get(column_name='学修课程'));
        serializer = SeminarSerializer(model, many=True)
        return render(request, 'seminars.html',{
            'result_code':1, #查到结果，标识位为1
            'seminar_list':  serializer.data,
        })
    except ObjectDoesNotExist:
        return render(request, 'seminars.html', {
                     'result_code':0, #未查到结果，标识位为0
                 })
    
def SeminarsSingleView(request,seminar_title):
    if(seminar_title=='graphics.php'):
        return render(request, 'seminars-single.html', {
                     'result_code':0, #未查到结果，标识位为0
                 })
    else:
            try:
                 model = Activity.objects.get(activity_title=seminar_title)
                 serializer = SeminarSerializer(model, many=False)
                 return render(request, 'seminars-single.html',serializer.data)
            except ObjectDoesNotExist:
                 return render(request, 'seminars-single.html', {
                     'result_code':0, #未查到结果，标识位为0
                 })

def SeminarsEnrollView(request):
    if request.method == 'POST':
        seminar_title = request.POST.get('seminar_title')
        name = request.POST.get('name')
        email = request.POST.get('email')
        try:    
            seminar = Seminar.objects.get(seminar_title=seminar_title);
            SeminarEnroll.objects.create(seminar=seminar,name=name,email=email)
        except IntegrityError:
            return HttpResponse('您已经报名参见，请勿重复报名！')
        return HttpResponse('报名成功，欢迎报名参加！')
     
    else:
        return HttpResponse('报名失败')


def WorkshopView(request):
    try:
        model = Activity.objects.filter(activity_column=ActivityColumn.objects.get(column_name='交流活动'));
        return render(request, 'workshops.html',{
            'result_code':1, #查到结果，标识位为1
            'workshop_list': model
        })
    except ObjectDoesNotExist:
        return render(request, 'workshops.html', {
                     'result_code':0, #未查到结果，标识位为0
                 })
    
def WorkshopsSingleView(request,workshop_title):
    if(workshop_title=='graphics.php'):
        return render(request, 'workshops-single.html', {
                     'result_code':0, #未查到结果，标识位为0
                 })
    else:
            try:
                 model = Activity.objects.get(activity_title=workshop_title);
                 speakers = Speaker.objects.all();
                 return render(request, 'workshops-single.html', {
                     'workshop': model,
                     'speakers': speakers
                 })
            except ObjectDoesNotExist:
                 return render(request, 'workshops-single.html', {
                     'result_code':0, #未查到结果，标识位为0
                 })

def RecordView(request):
    try:
        model = Activity.objects.filter(activity_column=ActivityColumn.objects.get(column_name='对外活动'));
        return render(request, 'records.html',{
            'result_code':1, #查到结果，标识位为1
            'record_list': model
        })
    except ObjectDoesNotExist:
        return render(request, 'records.html', {
                     'result_code':0, #未查到结果，标识位为0
                 })
    
def RecordsSingleView(request,record_title):
    if(record_title=='graphics.php'):
        return render(request, 'records-single.html', {
                     'result_code':0, #未查到结果，标识位为0
                 })
    else:
            try:
                 model = Activity.objects.get(activity_title=record_title);
                 return render(request, 'records-single.html', {
                     'record': model
                 })
            except ObjectDoesNotExist:
                 return render(request, 'records-single.html', {
                     'result_code':0, #未查到结果，标识位为0
                 })



class DisclaimerView(TemplateView):
    template_name = 'disclaimer.html'
    
class VideosView(TemplateView):
    template_name = 'videos.html'   
   
def email_sub(request):
    if request.method == 'POST':
        newsletter_email = request.POST.get('newsletter_email')
        newsletter_zip = request.POST.get('newsletter_zip')
        try:    
            EmailSub.objects.create(email_address=newsletter_email,name=newsletter_zip)
        except IntegrityError:
            return HttpResponse('您已经注册，请勿重复注册！')
        try:
            send_mail(
            '欢迎订阅龙泉大悲寺资讯',
            '欢迎订阅龙泉大悲寺资讯，我们将定期向您推送最新资讯',
            'durui.9190@gmail.com',#发送邮件的邮箱地址，需修改为龙泉大悲寺的邮箱地址。邮箱设置参考https://segmentfault.com/q/1010000008458788
            [newsletter_email],#接收邮件的邮箱地址
            fail_silently=False,)
        except SMTPAuthenticationError:
            return HttpResponse('欢迎订阅邮件新闻')
        return HttpResponse('欢迎订阅邮件新闻！')
     
    else:
        return HttpResponse('邮件订阅失败')
    
def to_be_volunteer(request):
    if request.method == 'POST':
        family_name = request.POST.get('family_name')
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        country = request.POST.get('country')
        zip = request.POST.get('zip')
        telephone = request.POST.get('telephone')
        mobilephone = request.POST.get('mobilephone')
        skills = request.POST.get('skills')
        contact_message = request.POST.get('contact_message')
             
        try:   
            Volunteers.objects.create(family_name=family_name,first_name=first_name,email=email,address1=address1,address2=address2,city=city,country=country,zip=zip,telephone=telephone,mobilephone=mobilephone,skills=skills,contact_message=contact_message)
        except IntegrityError:
            return HttpResponse('您已经注册为义工，请勿重复注册！')
        try:
            send_mail(
            '欢迎加入龙泉大悲寺志愿者',
            '欢迎加入龙泉大悲寺志愿者，如有需要我们会与您联系，谢谢。',
            'durui.9190@gmail.com',#发送邮件的邮箱地址，需修改为龙泉大悲寺的邮箱地址。邮箱设置参考https://segmentfault.com/q/1010000008458788
            [email],#接收邮件的邮箱地址
            fail_silently=False,
            )
        except SMTPAuthenticationError:
            return HttpResponse('欢迎加入龙泉大悲寺志愿者')
        return HttpResponse('欢迎加入龙泉大悲寺志愿者，我们已向您的邮箱发送邮件！')
     
    else:
        return HttpResponse('提交失败！')
