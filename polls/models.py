from django.db import models

class Sondage(models.Model):
    question = models.TextField()
    res_1 = models.CharField(max_length=255)
    res_2 = models.CharField(max_length=255)
    res_3 = models.CharField(max_length=255)
    count_res_1 = models.PositiveIntegerField(default=0)
    count_res_2 = models.PositiveIntegerField(default=0)
    count_res_3 = models.PositiveIntegerField(default=0)
    add_le = models.DateTimeField(auto_now_add=True)

    def total(self):
        return self.count_res_1 + self.count_res_2 + self.count_res_3

    def __str__(self):
        if len(self.question) >= 25:
            return ('%s') %(self.question)[0:25]
        else :
            return '%s' %(self.question)

# Create your models here.
