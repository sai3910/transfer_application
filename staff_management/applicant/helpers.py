from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class PaginationHelper(object):
    """
    Use this helper for pagination
    """
    def paginate(self, request, list):
        page_size = request.GET.get('page_size') or 10
        page = request.GET.get('page')
        paginator = Paginator(list, page_size)
        try:
            list = paginator.page(page)
        except PageNotAnInteger:
            list = paginator.page(1)
        except EmptyPage:
            list = paginator.page(paginator.num_pages)
        return list