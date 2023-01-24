from rest_framework.pagination import CursorPagination


class CustomPagination(CursorPagination):
    page_size_query_param = 'page_size'
    ordering = '-created_at'
