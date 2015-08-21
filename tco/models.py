from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.
class Result(models.Model):
	grand_total = models.IntegerField()
	total_reduction = models.IntegerField()

class Questions(models.Model):
	size_choice = (
        ('0', 'Average'),
        ('1', '1 person'),
        ('2', '2 person'),
        ('3', '3 person'),
        ('4', '4 person'),
        ('5', '5 person'),
        )
	income_choices = (
		('1',	'Average'),
		('2',	'Less than $10,000'),
		('3',	'$10,000 to $19,999'),
		('4',	'$20,000 to $29,999'),
		('5',	'$30,000 to $39,999'),
		('6',	'$40,000 to $49,999'),
		('7',	'$50,000 to $59,999'),
		('8',	'$60,000 to $79,999'),
		('9',	'$80,000 to $99,999'),
		('10',	'$100,000 to $119,999'),
		('11',	'$120,000 or more'),
		)
	location_mode_choice = (
		('1',	'ZIP code'),
		('2',	'City'),
		('3',	'County'),
		('4',	'State'),
		)
	input_location = models.CharField(max_length=5,null = False, blank = False)
	input_income = models.CharField(max_length=20,null = False, blank = False, choices = income_choices)
	input_location_mode = models.CharField(max_length=10,null = False, blank = False, choices = location_mode_choice)
	input_size = models.CharField(max_length = 10, null = False, blank = False, choices = size_choice)


	def __unicode__(self):
		return smart_unicode(self.input_location)