from django.db import models

# Create your models here.
class Squirrel(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    unique_squirrel_id = models.CharField(max_length = 255)
    hectare = models.CharField(max_length = 255)
    PM = 'PM'
    AM = 'AM'
    SHIFT_CHOICES = (
            (PM,'PM'),
            (AM,'AM'),
            )
    shift = models.CharField(
            max_length=255,
            choices=SHIFT_CHOICES,
            default=AM,
            )
    date = models.DateField()
    hectare_squirrel_number = models.IntegerField()
    age = models.CharField(max_length = 255)
    primary_fur_color = models.CharField(max_length = 255)
    highlight_fur_color = models.CharField(max_length = 255)
    combination_of_primary_and_highlight_color = models.CharField(max_length = 255)
    color_notes = models.TextField()
    location = models.CharField(max_length = 255)
    above_ground_sighter_measurement = models.CharField(max_length = 255)
    specific_location = models.CharField(max_length = 255)
    running = models.BooleanField()
    chasing = models.BooleanField()
    climbing = models.BooleanField()
    eating = models.BooleanField)
    foraging = models.BooleanField()
    other_activities = models.CharField(max_length = 255)
    kuks = models.BooleanField()
    quaas = models.BooleanField()
    moans = models.BooleanField()
    tail_flags = models.BooleanField()
    tail_twitches = models.BooleanField()
    approaches = models.BooleanField()
    indifferent = models.BooleanField()
    runs_from = models.BooleanField()
    other_interactions = models.CharField(max_length = 255)
    lat_long = models.CharField(max_length = 255)
    zip_codes = models.CharField(max_length = 255)
    community_districts = models.IntegerField()
    borough_boundaries = models.IntegerField()
    city_council_districts = models.IntegerField()
    police_precincts = models.IntegerField()
