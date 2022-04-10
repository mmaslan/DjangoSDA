from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

#11. Utwórz pierwszą funkcję widoku drukująca/zwracająca hello world (pamietaj dodać ją do urls.py - moesz ustawić jej name).

def get_hello(request: WSGIRequest) -> HttpResponse:
    return HttpResponse("Hello world")

#12. Utwórz funkcję zwracającą listę stringów. Stringi niech będą losowym UUID dodawanym do listy. Lista niech posiada 10 elementów.
#    a) Zwróć listę jako HTTPResponse (musisz na liście zrobić json.dumps)
#    b) zwróć listę jako JsonResponse

def get_uuids_a(request: WSGIRequest) -> HttpResponse:
    uuids = [for _ in range(10)]
    return HttpResponse("Test")

def get_uuids_b(request: WSGIRequest) -> JsonResponse:
    uuids = [f"{uuid4()}" for _ in range(10)]
    return JsonResponse({"uuids":uuids})

def get_argument_free_path(request: WSGIRequest, x: int, y: str, z: str) -> HttpResponse:


    return HttpResponse(f"x = {x}, y = {y}. z = {z}")