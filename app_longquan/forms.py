 #coding=utf-8 
 
from django.forms import ModelForm
from .models import Comment 
 
class CommentForm(ModelForm):
    #自定义ModelForm的内容  
    class Meta:  
        #该ModelForm参照Model: Node  
        model = Comment  
        #在Form中不显示node_signer这个字段  
        exclude = ['comment_time','article','comment_comment'] 