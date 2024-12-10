from django.db import models
from django.urls import reverse

# Create your models here.
# a models are used to define database structure as python classes

class Journalist(models.Model):
	"""generic model of a journalist"""
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)

	def __str__(self):
		return f"{self.first_name} {self.last_name}"


class Article(models.Model):
	"""Generic model of a news articles"""
	title = models.CharField(max_length=100)
	content = models.TextField()
	"""	relational field
		foreignKey is used to estabilish a relation between the journalist and the article
		the relation is many-to-one(many articles written by one journalist)
		this relation field requires 2 position arguments: the class to which the model is related and the on_delete method
		with on_delete=models.CASCADE if we delete the journalist all the articles (written by that jornalist) are deleted
		releted_name define the name of the reverse relationship.
		for example we can retrive a specific article of the journalist with journalist.articles
	"""
	journalist = models.ForeignKey(Journalist, on_delete=models.CASCADE, related_name="articles")

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("article_detail", kwargs={"pk" : self.pk})
