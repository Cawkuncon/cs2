from rest_framework import pagination


class ListPagination(pagination.PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 1000


class NoticePagination(pagination.PageNumberPagination):
    page_size = 10
