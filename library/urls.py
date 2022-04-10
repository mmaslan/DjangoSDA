from django.contrib import admin
from django.urls import path

from books.view import get_hello, get_uuids_a, get_argument_from path

urlpatterns = [
    path('admin'/, admin.site.urls)
    path('', set_hello),
    path('uuids-a', get_uuids_a),
    path('uuids-b', get_uuids_b)
    path('path_args/<int:x>/<str:y>/<slug:z>', get_argument_from_path, name="get_from_path")
]