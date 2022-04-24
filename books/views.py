from uuid import uuid4

from django.core.exceptions import BadRequest
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from books.models import BookAuthor, Category, Book


class AuthorListBaseView(View):
    template_name = "author_list.html"
    queryset = BookAuthor.objects.all()  # type: ignore

    def get(self, request: WSGIRequest, *args, **kwargs):
        context = {"authors": self.queryset}
        return render(request, template_name=self.template_name, context=context)


class CategoryListTameplateView(TemplateView):
    template_name = "category_list.html"
    extra_context = {"categories": Category.objects.all()} # type: ignore


class BooksListView(ListView):
    template_name = "books_list.html"
    model = Book
    paginate_by = 10


# 11.

def get_hello(request: WSGIRequest) -> HttpResponse:
    hello = "Hello world!"
    return render(request, template_name="Hello_world.html", context={"hello_var": hello})

# 12.

def get_uuids_a(request: WSGIRequest) -> HttpResponse:
    uuids = [f"{uuid4()}" for _ in range(10)]
    return render(request, template_name="uuids_a.html", context={"elements": uuids})
    #return HttpResponse(f"uuids={uuids}")

def get_uuids_b(request: WSGIRequest) -> JsonResponse:
    uuids = [f"{uuid4()}" for _ in range(10)]
    return JsonResponse({"uuids":uuids})

# 13.

def get_argument_from_path(request: WSGIRequest, x: int, y: str, z: str) -> HttpResponse:
    return HttpResponse(f"x = {x}, y = {y}. z = {z}")

# 14.

def get_argument_from_query(request: WSGIRequest, x: int, y: str, z: str) -> HttpResponse:
    a = request.GET.get("a")
    b = request.GET.get("b")
    c = request.GET.get("c")
    print(type(int(a)))
    return HttpResponse("Test")

# 15.

@csrf_exempt
def check_http_query_type(request: WSGIRequest) -> HttpResponse:
    #query_type = "Unknown"
    #if request.method == "GET":
    #    query_type = "To jest GET"
    # elif request.method == "PAST":
    #     query_type = "To jest PAST"
    # elif request.method == "PUT":
    #     query_type = "To jest PUT"
    # elif request.method == "DELETE":
    #     query_type = "To jest DELETE"
    # return HttpResponse(query_type)
    return render(request, template_name="method.html", context={})

# 21.

def get_headers(request: WSGIRequest) -> HttpResponse:
    our_headers = request.headers

    return JsonResponse({"headers": dict(our_headers)})

# 22.

@csrf_exempt
def raise_error_for_fun(request: WSGIRequest) -> HttpResponse:
    if request.method != "GET":
        raise BadRequest("method not allowes")
    return HttpResponse("Wszystko GIT")



