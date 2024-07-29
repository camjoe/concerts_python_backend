from django.db import models

# Create your models here.
class Band(models.Model):
  name = models.CharField(max_length=100, primary_key=True)
  image_url = models.URLField()

  class Meta:
    db_table = "band"

class Venue(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)

  class Meta:
    db_table = "venue"

class Concert(models.Model):
  id = models.AutoField(primary_key=True)
  headliner_band = models.ForeignKey(Band, on_delete=models.CASCADE)
  supporting_bands = models.ManyToManyField(Band, related_name="supporting_concert")
  date = models.DateTimeField()
  ticket_price = models.DecimalField(max_digits=7, decimal_places=2)
  venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

  class Meta:
    ordering = ['date']
    db_table = "concert"