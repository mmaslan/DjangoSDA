from django.urls import path

from books.views import get_uuids_a, get_uuids_b, get_argument_from_path, get_argument_from_query, \
    check_http_query_type, get_headers, raise_error_for_fun, AuthorListBaseView, CategoryListTameplateView, \
    BooksListView, BookDetailsView, CategoryCreateFormView, AuthorCreateView, AuthorUpdateView, BookCreateView, \
    BookUpdateView

urlpatterns = [
    path('uuids-a', get_uuids_a),
    path('uuids-b', get_uuids_b),
    path('path-args/<int:x>/<str:y>/<slug:z>/', get_argument_from_path, name="get_from_path"),
    path('query-args', get_argument_from_query, name="get_from_query"),
    path('query-types', check_http_query_type, name="check_query_type"),
    path('get-headers', get_headers, name="get_headers"),
    path('raise-error', raise_error_for_fun, name='raise-error'),
    path('author-list', AuthorListBaseView.as_view(), name='author-list'),
    path('category-list', CategoryListTameplateView.as_view(), name='category-list'),
    path('books-list', BooksListView.as_view(), name='books-list'),
    path('book-details/<int:pk>', BookDetailsView.as_view(), name="book-details"),
    path('category-create', CategoryCreateFormView.as_view(), name="category_create"),
    path('author-create', AuthorCreateView.as_view(), name="author_create"),
    path('author-update/<int:pk>/', AuthorUpdateView.as_view(), name="author_update"),
    path('book-create/', BookCreateView.as_view(), name="book_create"),
    path('book-update/<int:pk>/', BookUpdateView.as_view(), name="book_update"),
]