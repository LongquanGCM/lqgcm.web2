from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import Activity, ActivitySchedule, Speaker

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class EventScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivitySchedule
        fields = ('activity_schedule')
        
class EventSerializer(serializers.ModelSerializer):
    activity_schedule = serializers.StringRelatedField(many=True);
    
    class Meta:
        model = Activity
        fields = ('activity_title', 'activity_date', 'activity_location','activity_schedule', 'activity_description','activity_content','activity_publisher', 'activity_publish_time')

class SeminarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('activity_title', 'activity_location', 'activity_date','activity_description', 'activity_content','activity_photo')

