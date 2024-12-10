from django.shortcuts import render
from django.http import HttpResponse

from news.models import Article, Journalist
# Create your views here.
# # view rendered as httpResponse with html code
def home(request):

	return HttpResponse("<h1>Homepage!(core)</h1>")

