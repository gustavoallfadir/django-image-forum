from django.db import models
from django.contrib.auth.models import User

# Create your models here.


#---POST RELATED MODELS---
class Category(models.Model):
    "Model class for categories"

    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    def __str__(self):
        return self.name


class Post(models.Model):
    "Model class for posts or threads"

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()
    img = models.ImageField(upload_to='pictures/%Y/%m/%d/', blank=True, verbose_name='Picture')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    is_flagged = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


    def reply_count(self):
        count = Reply.objects.filter(parent=self.pk).count()
        reply = 'replies'
        if count == 1:
            reply = 'reply'
        return '%s %s' %(count,reply)

    def total_messages(self):
        replies = Reply.objects.filter(parent=self.pk).count()
        replies_on_replies = ReplyToReply.objects.filter(parent__parent=self.pk).count()
        count = replies + replies_on_replies
        messages = 'messages'
        if count == 1:
            messages = 'message'
        
        return '%s %s' %(count, messages) 


    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'


    def __str__(self):
        return '%s, %s, on %s' %(self.author, self.title, self.created)


class Reply(models.Model):
    "Model class for replys to posts"

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    img = models.ImageField(upload_to='pictures/%Y/%m/%d/', blank=True,verbose_name='Picture')
    parent = models.ForeignKey(Post, on_delete=models.CASCADE)        
    is_flagged = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    


    def get_replies(self):
        replies = ReplyToReply.objects.filter(parent=self.pk)
        return replies

    class Meta:
        verbose_name = 'reply'
        verbose_name_plural = 'replies'
    

    def __str__(self):
        return '%s, reply to %s, on %s' %(self.author, self.parent.title, self.created) 


class ReplyToReply(models.Model):
    "Model class for replies to replies"

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    parent = models.ForeignKey(Reply, on_delete=models.CASCADE) 
    is_flagged = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'reply on reply'
        verbose_name_plural = 'replies on reply'

    def __str__(self):
        return '%s, reply to %s, on %s' %(self.author,self.parent, self.created)


class Rule(models.Model):

    title = models.CharField(max_length=100)
    statement = models.TextField()

    def __str__(self):
        return self.title 

