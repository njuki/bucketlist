"""this class augments the default rest_framework.paginatio.LimitOffsetPagination"""

from rest_framework.pagination import LimitOffsetPagination


class PageLimit(LimitOffsetPagination):
    """
    Performs pagination based on diferrent criteria ie limit, or offset and limit
    """
    
    default_limit = 30
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 100