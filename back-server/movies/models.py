from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class Genre(models.Model):
    name = models.TextField()

class Movie(models.Model):
    title = models.CharField(max_length=50)   #제목
    popularity = models.FloatField()           #인기순
    genre_ids = models.ManyToManyField(Genre, related_name='movie_genre')  #장르
    release_date = models.DateField(null=True) # 
    vote_average = models.IntegerField() #평점
    vote_count = models.IntegerField() # 투표수
    overview = models.TextField() # 미리보기
    poster_path = models.TextField() # 이미지 파일

# class Rating(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ratings')
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
#     rates = models.PositiveIntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(10)])