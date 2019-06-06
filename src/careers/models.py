from django.db import models

class Career(models.Model):
	code = models.CharField(max_length=5)
	career = models.CharField(max_length=70)
	study_plan = models.CharField(max_length=20)

	def __unicode__(self):
		return self.career

	def __str__(self):
		return self.career