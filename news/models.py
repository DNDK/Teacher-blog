from django.db import models
from django.utils import timezone
import datetime

class Article(models.Model):
	title = models.CharField(max_length = 100)
	text = models.TextField()
	pub_date = models.DateTimeField(default = timezone.now())

	def __str__(self):
		return self.title
	


class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	author = models.CharField(max_length = 50)
	text= models.TextField()
	pub_date = models.DateTimeField(default = timezone.now())
	pub_date.editable = False

	def __str__(self):
		return self.text

