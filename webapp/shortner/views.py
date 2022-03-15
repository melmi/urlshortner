from dataclasses import asdict, dataclass
import json

from django.http import HttpResponseBadRequest, HttpResponsePermanentRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

from domain.boundaries.input.token_broker import TokenBroker


@dataclass
class UrlDto:
    url: str


@dataclass
class TokenDto:
    token: str


@method_decorator(csrf_exempt, name='dispatch')
class UrlAdder(View):
    def __init__(self, token_broker: TokenBroker):
        self.token_broker = token_broker

    def post(self, request):
        try:
            j = json.loads(request.body)
            in_dto = UrlDto(**j)
        except Exception:
            return HttpResponseBadRequest('invalid payload')
        token = self.token_broker.get_token(in_dto.url)
        out_dto = TokenDto(token)
        return JsonResponse(asdict(out_dto))


class UrlGetter(View):
    def __init__(self, token_broker: TokenBroker):
        self.token_broker = token_broker

    def get(self, request, token):
        url = self.token_broker.get_url(token)
        return HttpResponsePermanentRedirect(url)
