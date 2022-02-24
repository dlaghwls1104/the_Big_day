from django.db import models

class Visitor(models.Model) :
    name = models.CharField(max_length=6)
    memo = models.TextField()
    writedate = models.DateTimeField(auto_now_add=True) # auto_now

    def __str__(self):
        return "main {}-{}-{}".format(self.id, self.name, self.memo)
