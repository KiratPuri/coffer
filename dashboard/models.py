from django.db import models

# Create your models here.

class data(models.Model):
    end_year = models.CharField(max_length=50, blank=True)
    intensity = models.IntegerField(null=True)
    sector = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    insight = models.TextField()
    url = models.URLField()
    region = models.CharField(max_length=100)
    start_year = models.CharField(max_length=50, blank=True)
    impact = models.TextField(blank=True)
    added = models.DateTimeField(null=True)
    published = models.DateTimeField(null=True)
    country = models.CharField(max_length=100)
    relevance = models.IntegerField(null=True)
    pestle = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    title = models.TextField()
    likelihood = models.IntegerField(null=True)

    def __str__(self):
        return self.added
