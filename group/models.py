from django.db import models

class Recruit(models.Model):
    COMPETITION_CHOICES=[
        ('2022년 강서구 빅데이터 활용 공모전', '2022년 강서구 빅데이터 활용 공모전'),
        ('2022년 노원구 빅데이터 활용 공모전', '2022년 노원구 빅데이터 활용 공모전'),
    ]
    subject = models.CharField(max_length=200)
    select = models.CharField(max_length=80, choices=COMPETITION_CHOICES, null=True)
    personnel = models.IntegerField(default=0)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject


class Applicant(models.Model):
    question = models.ForeignKey(Recruit, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject
