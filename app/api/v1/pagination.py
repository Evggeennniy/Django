from rest_framework.pagination import PageNumberPagination


class RatePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# class LimitOffsetPagination
# offset - specify how much data from the sample will be skipped.
# limit - after offset, the limit on the amount of data is applied.


class SourcePagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 20


class SupportPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20
