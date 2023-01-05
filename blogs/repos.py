from typing import Protocol, OrderedDict

from django.db.models import QuerySet

from blogs import models


class BlogReposInterface(Protocol):

    def create_blog(self, data: OrderedDict) -> models.Blog: ...

    def get_blogs(self) -> QuerySet[models.Blog]: ...

    def delete_blog(self, blog: models.Blog) -> None: ...


class BlogReposV1:

    def create_blog(self, data: OrderedDict) -> models.Blog:
        return models.Blog.objects.create(**data)

    def get_blogs(self) -> QuerySet[models.Blog]:
        return models.Blog.objects.all()

    def delete_blog(self, blog: models.Blog) -> None:
        blog.delete()
