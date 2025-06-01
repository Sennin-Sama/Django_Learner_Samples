from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

class WatchListPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'p'
    page_size_query_param = 'size'
    max_page_size = 10 
    last_page_strings = ['last','end']

class WatchlistLOPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'start'

class WatchlistCPagination(CursorPagination):
    page_size = 5
    ordering = 'created' 
    cursor_query_param = 'record'