from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from collections import Counter


from forum.models import Post, Reply, ReplyToReply
# Create your models here.


class UserMethod(User):
    "Proxy model class for creating User methods"
    #Don't change this part:
    class Meta:
        proxy = True

    def month_threads(self):
        current_year = timezone.now().year
        current_month = timezone.now().month
        month_threads = Post.objects.filter(
            author=self.pk).filter(
                created__year=current_year).filter(
                    created__month=current_month).count()
        return month_threads
    
    def month_messages(self):
        current_year = timezone.now().year
        current_month = timezone.now().month
        month_replies = Reply.objects.filter(
            author=self.pk).filter(
                created__year=current_year).filter(
                    created__month=current_month).count()
        month_replies_to_replies = ReplyToReply.objects.filter(
            author=self.pk).filter(
                created__year=current_year).filter(
                    created__month=current_month).count()
        month_messages = month_replies + month_replies_to_replies 

        return month_messages

    def total_posts(self):
        total_posts = Post.objects.filter(author=self.id).count()
        return total_posts

    def total_replies(self):
        replies = Reply.objects.filter(author=self.id).count()
        replies_to_replies = ReplyToReply.objects.filter(author=self.id).count()
        total_replies = replies + replies_to_replies

        return total_replies

    def total_messages(self):
        posts =  Post.objects.filter(author=self.id).count()
        replies =  Reply.objects.filter(author=self.id).count()
        replies_to_replies = ReplyToReply.objects.filter(author=self.id).count()
        total_messages = posts + replies + replies_to_replies

        return total_messages


    def total_flagged_threads(self):
        total_flagged_threads = Post.objects.filter(
            author=self.id).filter(
                is_flagged=True).count()

        return total_flagged_threads

    def fav_cat(self):        
        posts = Post.objects.filter(author=self.id).values_list('category__name')
        count = Counter(posts)
        most_common = count.most_common(1)[0]
        fav_cat = most_common[0][0]
        total = most_common[1]

        if total == 1:
            return "%s with %s post in total" %(fav_cat, total)
                    
        return "%s with %s posts in total" %(fav_cat, total)