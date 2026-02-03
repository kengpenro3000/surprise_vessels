from django.db import models
from .constants import DEFAULT_PARAMETERS


class VesselCategory(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="vessels_cats/", blank=True)
    description = models.TextField()
    parameters = models.JSONField(default = DEFAULT_PARAMETERS)
    # parameters = models.JSONField(default={"a": 0, "b": 0, "c": 0})
    # rating = models.IntegerField(default=0)

    def calculate_cat_rating(self):
        return Results.objects.filter(final_cat=self).count()

    def __str__(self):
        return self.name
    


    


class Vessel(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="vessels/", blank=True)
    description = models.TextField()
    category = models.ForeignKey(
        VesselCategory, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    question_text = models.CharField(max_length=200)


class Answer(models.Model):
    answer_text = models.CharField(max_length=200)
    weigth = models.JSONField(default="0 0 0")
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, default=None, null=True)


class Results(models.Model):
    final_answer = models.JSONField(default=DEFAULT_PARAMETERS)
    final_cat = models.ForeignKey(
        VesselCategory, on_delete=models.CASCADE, default=None, null=True)

    def calculate_nearest_cat(self, results):
        cats = []
        min = float("inf")
        min_cat_id = None
        for cat in VesselCategory.objects.all():
            for key in results.keys():
                rad_vector = (results[key] - cat.parameters[key])**2 
            rad_vector = rad_vector**(1/2)
            cats.append((cat, rad_vector))
            
        print(cats, "|" , results["a"], results["b"], results["c"])
        i = 0
        for par in cats:
            if min > par[1]:
                min = par[1]
                min_cat_id = i
            i += 1
        self.final_cat = cats[min_cat_id][0]



