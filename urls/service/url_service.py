from django.db.models import QuerySet

from urls.models import Url


class UrlService:

    def save_url(self, url: str) -> None:
        url_model = Url(long_name=url, popularity=1)
        url_model.save()
        short_url = self._url_shortener(url_model.id)
        url_model.short_name = short_url
        url_model.save()

    def _url_shortener(self, url_id: int) -> str:
        encoding_elements = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        new_url = ""
        base = len(encoding_elements)
        while url_id > 0:
            new_url += encoding_elements[url_id % base]
            url_id = url_id // base

        return new_url

    def get_most_popular_urls(self) -> QuerySet:
        return Url.objects.order_by("-popularity")[:100]

    def get_by_id(self, pk: int) -> Url:
        url = Url.objects.get(id=pk)
        url.popularity += url.popularity
        url.save()
        if url is None:
            raise Exception("Url not found")
        return url
