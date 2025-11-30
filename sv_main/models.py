from django.db import models

class VesselCategory(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="vessels_cats/" ,blank=True)
    description = models.TextField()
    rating = models.IntegerField(default=0)

class Vessel(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="vessels/" , blank=True)
    description = models.TextField()
    category = models.ForeignKey(VesselCategory, on_delete=models.CASCADE, default=None, null=True)

class Question(models.Model):
    question_text = models.CharField(max_length=200)

class Answer(models.Model):
    answer_text = models.CharField(max_length=200)
    weight_a = models.IntegerField()
    weight_b = models.IntegerField()
    weight_c = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=None, null=True)

class Results(models.Model):
    results = {"a" : 0, "b" : 0, "c" : 0}
    def decrees_for_one(self, a):
        self.results[a] += 1


