from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from urls.service.url_service import UrlService


# Create your views here.
class IndexView(generic.ListView):
    url_service = UrlService()
    context_object_name = "most_popular_urls"

    def get_queryset(self):
        return self.url_service.get_most_popular_urls()

    def post(self, request, *args, **kwargs):
        self.url_service.save_url(request.POST["url"])
        return HttpResponseRedirect(reverse("urls:index"))


class UrlView(generic.ListView):
    url_service = UrlService()

    def get(self, request, *args, **kwargs):
        url = self.url_service.get_by_id(kwargs["pk"])
        return HttpResponseRedirect(url.long_name)
