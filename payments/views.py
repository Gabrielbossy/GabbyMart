from django.http import HttpResponse
from .mpesa import get_access_token


def stk_push(request):

    token = get_access_token()

    return HttpResponse(
        f"Access Token: {token}"
    )