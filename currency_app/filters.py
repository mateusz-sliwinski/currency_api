"""Filters.py files."""
# 3rd-party
from rest_framework.pagination import LimitOffsetPagination


class LimitOffsetPaginationWithUpperBound(LimitOffsetPagination):  # noqa D101
    max_limit = 100
