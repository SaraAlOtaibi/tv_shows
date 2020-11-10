from django.db import models
import datetime
# Create your models here.

class ShowManager(models.Manager):
    def validate(self, post_data):
        errors = []
        if len(post_data['the_title']) < 1:
            errors.append('Please fill the title field ')
        elif len(post_data['the_title']) < 2:
            errors.append('Title field can\'t be less than two characters')
        if len(post_data['network']) < 1:
            errors.append('Please fill the network field ')
        elif len(post_data['network']) < 3:
            errors.append('Network field can\'t be less than three characters')
        if len(post_data['date']) < 1:
            errors.append('Please fill the date field ')
        elif not self.has_expired(post_data['date']):
            errors.append('Date is not valid, it should be in the past ')
        if len(post_data['desc']) > 0 and len(post_data['desc']) < 10:
            errors.append('The description can\'t be less than 10 characters' )
        if Shows.objects.filter(title=post_data['the_title']).exists():
            errors.append('The title already exists' )


        return errors

    def has_expired(self, date):
        #print('TYPE IS !!!!!!!! ' , type(date))
        #print(date)
        ##print(type( date.strftime('%Y-%m-%d')) )
        #print ( datetime.date.strftime(date, '%Y-%m-%d').date() )
        #print ( type( datetime.date.strftime(date, '%Y-%m-%d').date() ))
        #print(date.strftime('%Y-%m-%d'))
        #return True
        #date < datetime.datetime.now()
        return datetime.datetime.strptime(date, "%Y-%m-%d") < datetime.datetime.now()


class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()

    def __str__(self):
        return f"<Show object: ID : {self.id}, Name : {self.title}, Network : {self.network}, Description {self.desc}, Release Date {self.release_date}>\n"

