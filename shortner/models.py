from django.db import models
from .domain.entities.url_token import UrlToken as DomainUrlToken


class UrlToken(models.Model):
    url = models.CharField(max_length=1000)
    token = models.CharField(max_length=50, db_index=True)

    @staticmethod
    def from_domain(data: DomainUrlToken):
        result = UrlToken(url=data.url, token=data.token)
        return result

    @staticmethod
    def to_domain(model) -> DomainUrlToken:
        result = DomainUrlToken(model.url, model.token)
        return result
