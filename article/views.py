from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'article/index.html')
def index(request):
    all_article=Article.object.all(                                                                                                                   )