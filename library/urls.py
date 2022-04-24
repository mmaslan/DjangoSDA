from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from books.views import get_hello


urlpatterns = [
    path('', get_hello),
    path('books/', include('books.urls')),
    # path('uuids-a', get_uuids_a),
    # path('uuids-b', get_uuids_b),
    # path('query-args/<int:x>/<str:y>/<slug:z>/', get_argument_from_path, name="get_from_path"),
    # path('query-args', get_argument_from_query, name="get_from_query"),
    # path('check_type', check_http_query_type, name="get_from_type"),
    # path('get-header', get_headers, name="get_headers"),
    # path('raise-error', raise_error_for_fun, name="raise-error"),
]

# if settings.DEBUG:
#     urlpatterns.append(path('admin/', admin.site.urls))