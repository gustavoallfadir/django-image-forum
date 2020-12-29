from django.db import models

# Create your models here.

class Message(models.Model):

    remitent = models.EmailField(verbose_name='email')
    subject = models.CharField(max_length=50)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(
        upload_to='messages/%Y/%m/%d/', 
        blank=True,
        verbose_name='picture',
    )
    answered = models.BooleanField(default=False)

    class meta:

        verbose_name = 'message'
        verbose_name_plural = 'messages'

    def __str__(self):
        return '%s on %s' %(self.remitent, self.created)

