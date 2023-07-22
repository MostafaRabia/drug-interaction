from django.db import models

class Drug(models.Model):
    name = models.CharField(max_length=50)
    active_substances = models.ManyToManyField("ActiveSubstance", related_name='drugs')

    def __str__(self) -> str:
        return self.name

class ActiveSubstance(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Disease(models.Model):
    name = models.CharField(max_length=50)
    active_substances = models.ManyToManyField(ActiveSubstance, related_name='diseases', through='ActiveSubstanceDisease')

    def __str__(self) -> str:
        return self.name

class ActiveSubstanceDisease(models.Model):
    active_substance = models.ForeignKey(ActiveSubstance, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    more_information = models.CharField(max_length=150, null=True)
