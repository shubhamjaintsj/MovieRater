from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import math

class Movie(TimeStampedModel):
    title = models.CharField(max_length=355)
    description = models.TextField(blank=True)

    def no_of_rating(self):
        raitings = Raiting.objects.filter(movie=self)
        return len(raitings)

    def avg_rating(self):
        raitings = Raiting.objects.filter(movie=self)

        _sum = sum([x.stars for x in raitings])
        _avg = _sum/len(raitings) if len(raitings) else 0

        return _avg

    def __str__(self):
        return f"{self.id} : {self.title}"

class Raiting(TimeStampedModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'movie'))
        index_together = (('user', 'movie'))