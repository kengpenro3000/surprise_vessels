from django.db import models


class VesselCategory(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="vessels_cats/", blank=True)
    description = models.TextField()
    parameters = models.JSONField(default={"a": 0, "b": 0, "c": 0})
    rating = models.IntegerField(default=0)


class Vessel(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="vessels/", blank=True)
    description = models.TextField()
    category = models.ForeignKey(
        VesselCategory, on_delete=models.CASCADE, default=None, null=True)


class Question(models.Model):
    question_text = models.CharField(max_length=200)


class Answer(models.Model):
    answer_text = models.CharField(max_length=200)
    weight_a = models.IntegerField()
    weight_b = models.IntegerField()
    weight_c = models.IntegerField()
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, default=None, null=True)


class Results(models.Model):
    final_answer = models.JSONField(default={"a": 0, "b": 0, "c": 0})
    final_cat = models.ForeignKey(
        VesselCategory, on_delete=models.CASCADE, default=None, null=True)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if not self.results:
    #         results = {"a" : 0, "b" : 0, "c" : 0}

    def increment_for_one(self, a):
        self.results[a] += 1
        self.save()

    def increment(self, a, x):
        rslt = self.results
        rslt[a] += x
        self.update(results=rslt)

    def calculate_nearest_cat(self, results):
        cats = []
        min = float("inf")
        min_cat_id = None
        for cat in VesselCategory.objects.all():
            rad_vector = ((results["a"] - cat.parameters["a"])**2 + (results["b"] -
                          cat.parameters["b"])**2 + (results["c"] - cat.parameters["c"])**2)**(1//2)
            cats.append((cat.name, rad_vector))

        for par in cats:
            i = 0
            if min > par[1]:
                min_cat_id = i
            i += 1
        self.final_cat = cats[min_cat_id][0]
        # найти радиус-векторы до всех категорий
        # вынуть все поля с параметрами категорий
        # форчиком пройтись по ним, посохранять пары [(категория, радиус-вектор)] (просто список с кортежами)
        # найти наименьший

        # вкусно:
        # min(a, key = lambda elem: elem[1])
        # напиши невкусно

        # self.final_cat =   заглушка
