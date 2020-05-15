from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect

from .models import Article

def index(request):
	lastest_articles_list = Article.objects.order_by('-pub_date')[:10]
	context = {'lastest_articles_list':lastest_articles_list}
	return render(request, 'news/index.html', context)

def detail(request, article_id):
	article = get_object_or_404(Article, pk = article_id)
	comments = article.comment_set.order_by('-pub_date')[:20]
	context = {'article': article, 'comments':comments,}
	return render(request, 'news/detail.html', context)

def leave_comment(request, article_id):
	article = get_object_or_404(Article, pk = article_id)
	article.comment_set.create(author = request.POST['author'], text = request.POST['text'])

	return HttpResponseRedirect( reverse('news:detail', args = (article_id,)) )
