from unittest.mock import Mock

from django.test import TestCase
from urls.models import Url
from urls.views import IndexView


class AnimalTestCase(TestCase):
    def setUp(self):
        Url.objects.create(short_name="a", long_name="http://www.google.com", popularity=1)
        Url.objects.create(short_name="b", long_name="http://www.google.com", popularity=1)

    def test_get_list_of_urls(self):
        response = IndexView().get_queryset()

        assert len(response) == 2

    def test_add_url(self):
        long_name = "http://www.google.com/something"
        mock = Mock(POST={"url": long_name})

        IndexView().post(mock)

        url = Url.objects.get(long_name=long_name)

        assert url is not None
        assert url.popularity == 1
        assert url.short_name is not None
