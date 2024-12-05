from django.shortcuts import render
from django.http import HttpResponse

from news.models import Article, Journalist
# Create your views here.

def home(request):
	articles_title =[]
	articles_content =[]
	journalists =[]

	for a in Article.objects.all():
		articles_title.append("<br>")
		articles_title.append(a.title)
		articles_content.append("<br>")
		articles_content.append(a.content)

	for j in Journalist.objects.all():
		journalists.append("<br>")
		journalists.append(j.first_name +" " + j.last_name)

	response = "<h3>Article titles are: </h3>" + " ".join(articles_title) + "<h3>Contents are: </h3>"  +  "".join(articles_content) + "<h3>Journalists are: </h3>" +"".join(journalists)
	print(response)

	return HttpResponse(f"<h1>Homepage!</h1><br><p>{response}</p>")

