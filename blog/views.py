from django.shortcuts import render, get_object_or_404
from .models import article
from .forms import comment_form
from django.core import mail
# Create your views here.


def detail(request):
    all_blog = article.objects.all()
    context = {
        'all_blog': all_blog
    }
    return render(request, 'blog-grid.html', context)


def blog(request, num):
    Single_blog = get_object_or_404(article, pk=num)
    all_coments = Single_blog.coment.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        commentform = comment_form(data=request.POST)
        if commentform.is_valid():
            new_comment = commentform.save(commit=False)
            new_comment.post = Single_blog
            new_comment.save()
            mail.send_mail(
                'new comment',
                'you have new comment on website',
                'a8888ralireza@gmail.com',
                ['a8888ralireza@gmail.com'],
                fail_silently=False
            )
    else:
        commentform = comment_form()

    context = {
        'single_blog': Single_blog,
        'all_coments': all_coments,
        'new_comment': new_comment,
        'commentform': commentform,
    }
    return render(request, 'blog-single.html', context)
