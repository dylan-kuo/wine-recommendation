from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg


class Wine(models.Model):
    name = models.CharField(max_length=200)

    def average_rating(self):
        return self.review_set.aggregate(Avg('rating'))['rating__avg']
        return np.mean(all_ratings)
        
    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)


class Cluster(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)

    def get_members(self):
        return "\n".join([u.username for u in self.users.all()])
    