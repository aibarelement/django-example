from django.forms import model_to_dict
from django.http import JsonResponse
from blogs.models import Blog


def index(request):
    queryset = Blog.objects.filter(title__in=request.GET.getlist('title', []))
    blogs = [model_to_dict(b) for b in queryset]
    return JsonResponse(blogs, safe=False)


def create_blog(request):
    blog = Blog.objects.create(
        title=request.POST.get('title'),
        body=request.POST.get('body')
    )
    return JsonResponse(model_to_dict(blog), safe=False)


def delete_blog(request, *args, **kwargs):
    Blog.objects.get(**kwargs).delete()

    return JsonResponse({}, safe=False, status=204)
