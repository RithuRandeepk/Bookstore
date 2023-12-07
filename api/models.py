from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.


class Books(models.Model):
    bookname=models.CharField(unique=True,max_length=200)
    author=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    description=models.CharField(max_length=200)
    category=models.CharField(max_length=200)

    @property
    def avg_rating(self):
        ratings = self.reviews_set.all().values_list("rating", flat=True)

        if ratings:

            return sum(ratings) / len(ratings)
        else:
            return 0

    def review_count(self):

        ratings = self.reviews_set.all().values_list("rating", flat=True)

        if ratings:
            return len(ratings)
        else:
            return 0

    def __str__(self):
        return self.name


class Carts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Books, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class Reviews(models.Model):
    product = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comments = models.CharField(max_length=200)

    def __str__(self):
        return self.comments

