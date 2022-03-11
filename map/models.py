from django.db import models

# 이름 url 시간 홈페이지 url

class Cafe(models.Model):
    name = models.CharField(max_length=200)
    kakaourl = models.URLField(max_length=200)
    pageurl = models.URLField(max_length=200)

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=200)
    kakaourl = models.URLField(max_length=200)
    pageurl = models.URLField(max_length=200)

    def __str__(self):
        return self.name

class Notebook(models.Model):
    name = models.CharField(max_length=200)
    kakaourl = models.URLField(max_length=200)
    pageurl = models.URLField(max_length=200)

    def __str__(self):
        return self.name


