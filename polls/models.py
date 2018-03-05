import datetime
from django.db import models
from django.utils import timezone
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return (self.pub_date >= timezone.now() - datetime.timedelta(days = 1) and self.pub_date <= timezone.now() )

    was_published_recently.admin_order_field = 'pub_date' #daje mozliwosc sortowanie po paramaetrzy pub date, domysnie nie sortuje - nie jest wspierane
    #was_published_recently.boolean = True #zmienia na znaczki (dodaje sposob pokazywania dla boolean)
    was_published_recently.short_description = 'Published recently?'  #dodaje nazwe
class Choices(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text + ', votes: ' + str(self.votes)
# Create your models here.
