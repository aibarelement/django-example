from typing import Protocol, OrderedDict

from django.db.models import QuerySet

from accounts import repos, models


class AccountServicesInterface(Protocol):
    account_repos: repos.AccountReposInterface

    def get_accounts(self, action: str) -> QuerySet[models.Account]: ...

    def create_account(self, data: OrderedDict) -> None: ...


class AccountServicesV1:
    account_repos: repos.AccountReposInterface = repos.AccountReposV1()

    def get_accounts(self, action: str) -> QuerySet[models.Account]:
        return self.account_repos.get_accounts(action=action)

    def create_account(self, data: OrderedDict) -> None:
        try:
            self.account_repos.create_account(data=data)
        except Exception as e:
            print('error!')
