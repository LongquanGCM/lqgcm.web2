from django.conf.urls import url, include

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

app_name = 'app_longquan'
urlpatterns = [
    url(r'^users/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    # ex: /longquan/
    url(r'^$', views.HomePageView.as_view(), name='home'),
    
    url(r'^home/$', views.HomePageView.as_view(), name='home'),
    
    
    
    url(r'^venerable-single-blog/(?P<pk>[0-9]+)$', views.VenerableSingleBlogView.as_view(), name='venerable-single-blog'),
    
    url(r'^venerable-single-blog/$', views.VenerableSingleBlogView.as_view(), name='venerable-single-blog'),
        
    # ex: /longquan/about/
    # the 'name' value as called by the {% url %} template tag in html file
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    
    # ex: /longquan/team/
    # the 'name' value as called by the {% url %} template tag in html file
    url(r'^team/$', views.TeamView.as_view(), name='team'),
    
    # ex: /longquan/get-involved/
    # the 'name' value as called by the {% url %} template tag in html file
    url(r'^get-involved/$', views.GetInvolvedView.as_view(), name='get-involved'),

    # ex: /longquan/contact/
    # the 'name' value as called by the {% url %} template tag in html file
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    
    # >>>>>>>>>>>>>>
    # >>> tested >>>
    # >>>>>>>>>>>>>>
    # ex: /longquan/venerable-*/
    # the 'name' value as called by the {% url %} template tag in html file
    url(r'^venerable-profile/$', views.VenerableProfileView.as_view(), name='venerable-profile'), 
    url(r'^venerable-blog/$', views.VenerableBlogView.as_view(), name='venerable-blog'),
    
    url(r'^venerable-fayu/$', views.FayuView, name='venerable-fayu'),
    url(r'^venerable-fayu-single/([\S\s]+)/$', views.FayuSingleView, name='venerable-fayu-single'),
    
    url(r'^venerable-dayi/$', views.DayiView, name='venerable-dayi'),
    url(r'^venerable-dayi-single/([\S\s]+)/$', views.DayiSingleView, name='venerable-dayi-single'),
    
    url(r'^xianer/$', views.XianerView, name='xianer'),
    url(r'^xianer-single/([\S\s]+)/$', views.XianerSingleView, name='xianer-single'),
    
    # ex: /longquan/events/
    url(r'^events/$', views.EventView, name='events'),
    # to make the events-single link support any string (incl. chinese) and whitespace, but not # symbol
    url(r'^events-single/([\S\s]+)/(\S+)/$', views.EventsSingleView, name='events-single'),
    url(r'^sidebar_upcoming_events.html/$', views.UpcomingEventView, name='sidebar_upcoming_events'),
    url(r'^apply_event/$', views.EventsEnrollView, name='apply_event'),
    
    # ex: /longquan/seminars/
    url(r'^seminars/$', views.SeminarView, name='seminars'),
    url(r'^seminars-single/(\S+)/$', views.SeminarsSingleView, name='seminars-single'),
    url(r'^apply_seminar/$', views.SeminarsEnrollView, name='apply_seminar'),

    # ex: /longquan/workshops/
    url(r'^workshops/$', views.WorkshopView, name='workshops'),
    url(r'^workshops-single/([\S\s]+)/$', views.WorkshopsSingleView, name='workshops-single'),

    # ex: /longquan/records/
    url(r'^records/$', views.RecordView, name='records'),
    url(r'^records-single/([\S\s]+)/$', views.RecordsSingleView, name='records-single'),
    
    # ex: /longquan/dabeishiye/
    url(r'^dabeishiye/$', views.DabeishiyeView, name='dabeishiye'),
    url(r'^dabeishiye-single/([\S\s]+)/$', views.DabeishiyeSingleView, name='dabeishiye-single'),

    # ex: /longquan/report/
    url(r'^report/$', views.ReportView, name='report'),
    url(r'^report-single/([\S\s]+)/$', views.ReportSingleView, name='report-single'),

    # ex: /longquan/records-share/
    url(r'^records-share/$', views.RecordShareView, name='records-share'),
    url(r'^records-share-single/([\S\s]+)/$', views.RecordShareSingleView, name='records-share-single'),

    # ex: /longquan/shareviews/
    url(r'^share-views/$', views.ShareViewsView, name='share-views'),
    url(r'^share-views-single/([\S\s]+)/$', views.ShareViewsSingleView, name='share-views-single'),
    # <<<<<<<<<<<<<<
    # <<< tested <<<
    # <<<<<<<<<<<<<<
    
    # ex: /longquan/disclaimer/
    # the 'name' value as called by the {% url %} template tag in html file
    url(r'^disclaimer/$', views.DisclaimerView.as_view(), name='disclaimer'),
    
    # ex: /longquan/videos/
    # the 'name' value as called by the {% url %} template tag in html file
    url(r'^videos/$', views.VideosView.as_view(), name='videos'),
    
    # ex: /longquan/about/
    # the 'name' value as called by the {% url %} template tag in html file
    url(r'^email_sub/$', views.email_sub, name='email_sub'),
    
    # ex: /longquan/about/
    # the 'name' value as called by the {% url %} template tag in html file
    url(r'^to_be_volunteer/$', views.to_be_volunteer, name='to_be_volunteer'),
]