from email.policy import default
from pydoc import pager
from rest_framework import pagination


class CustomPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'p'


class CustomPaginationLimitOffset(pagination.LimitOffsetPagination):
    default_limit = 2
    limit_query_param = 'l'
    offset_query_param = 'o'
    max_limit = 50

class CustomCursosPagination(pagination.CursorPagination):
    page_size=2
    cursor_query_param='c'
    ordering = '-id'