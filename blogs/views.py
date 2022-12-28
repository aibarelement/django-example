from django.http import JsonResponse

from blogs import models


def index(request, *args, **kwargs):
    title = request.GET.get('title')
    body = request.GET.get('body')
    blog = models.Blog.objects.create(title=title, body=body)

    return JsonResponse({
        'id': blog.id,
        'title': blog.title,
        'body': blog.body,
    })
