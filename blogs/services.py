from typing import Protocol, OrderedDict

from django.db.models import QuerySet

from blogs import models, repositories


class BlogServicesInterface(Protocol):
    repos: repositories.BlogRepositoriesInterface

    def create_blog(self, data: OrderedDict) -> models.Blog: ...

    def get_blogs(self) -> QuerySet[models.Blog]: ...


class BlogServicesV1:
    repos: repositories.BlogRepositoriesInterface = repositories.BlogRepositoriesV1()

    def create_blog(self, data: OrderedDict) -> models.Blog:
        print('create blog in service layer')
        return self.repos.create_blog(data=data)

    def get_blogs(self) -> QuerySet[models.Blog]:
        print('get blogs in service layer')
        return self.repos.get_blogs()
