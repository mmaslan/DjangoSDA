from uuid import uuid4

from django.core.exceptions import BadRequest, PermissionDenied
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

from books.forms import CategoryForm, AuthorForm, BookForm
from books.models import BookAuthor, Category, Book
import logging
logger = logging.getLogger(__name__)



class AuthorListBaseView(View):
    template_name = "author_list.html"
    queryset = BookAuthor.objects.all()  # type: ignore

    def get(self, request: WSGIRequest, *args, **kwargs):
        logger.debug(f"{request} ---")
        context = {"authors": self.queryset}
        return render(request, template_name=self.template_name, context=context)


class CategoryListTameplateView(TemplateView):
    template_name = "category_list.html"
    extra_context = {"categories": Category.objects.all()} # type: ignore


class BooksListView(ListView):
    template_name = "books_list.html"
    model = Book
    paginate_by = 10



class BookDetailsView(DetailView):
    template_name = "book_detail.html"
    model = Book

    def get_object(self, **kwargs):
        return get_object_or_404(Book, id=self.kwargs.get("pk"))



class CategoryCreateFormView(FormView):
    template_name = "category_form.html"
    form_class = CategoryForm
    success_url = reverse_lazy("category-list")

    def form_invalid(self, form):
        logger.critical(f"FROM CRITICAL ERROR. MORE INFO {form}")
        return super().form_invalid(form)

    def form_valid(self, form):
        result = super().form_valid(form)
        logger.info(f"form = {form}")
        logger.info(f"form.cleaned_data = {form.cleaned_data}")  # cleaned means with removed html indicators
        check_entity = Category.objects.create(**form.cleaned_data)
        logger.info(f"check_entity-id={check_entity.id}")
        return result

class AuthorCreateView(CreateView):
    template_name = "author_form.html"
    form_class = AuthorForm
    success_url = reverse_lazy("author-list")


class AuthorUpdateView(UpdateView):
    template_name = "author_form.html"
    form_class = AuthorForm
    success_url = reverse_lazy("author-list")

    def get_object(self, **kwargs):
        return get_object_or_404(BookAuthor, id=self.kwargs.get("pk"))

# 13. / 2

class BookCreateView(CreateView):
    template_name = "author_form.html"
    form_class = BookForm
    # success_url = reverse_lazy("book_list")

    def get_success_url(self):
        return reverse_lazy("books-list")

# 14. / 2

class BookUpdateView(UpdateView):
    template_name = "book_form.html"
    form_class = BookForm
    # success_url = reverse_lazy("book_list")

    def get_success_url(self):
        return reverse_lazy("books-list")

    def get_object(self, **kwargs):
        return get_object_or_404(Book, id=self.kwargs.get("pk"))


# 15. / 2

class BookDeleteView(DeleteView):
    template_name = "book_delete.html"
    model = Book
    # success_url = reverse_lazy("book_list")

    def get_success_url(self):
        return reverse_lazy("books-list")

    def get_object(self, **kwargs):
        return get_object_or_404(Book, id=self.kwargs.get("pk"))


# 11.

def get_hello(request: WSGIRequest) -> HttpResponse:
    user: User = request.user  # type: ignore
    # password = None if user.is_anonymous else user.password
    # email = None if user.is_anonymous else user.email
    # date_joined = None if user.is_anonymous else user.date_joined
    if not user.is_authenticated:
        # raise PermissionDenied()
        return HttpResponseRedirect(reverse('login'))
    is_auth: bool = user.is_authenticated
    hello = f"Hello {user.username}. Your password: {user.password}, your email: {user.email} and date you joined: {user.date_joined}!"
    return render(request, template_name="Hello_world.html", context={"hello_var": hello, "is_authenticated": is_auth})

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



