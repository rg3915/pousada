from django.shortcuts import resolve_url as r
from django.test import TestCase
from django.test.client import Client


class UrlTest(TestCase):

    def test_urls(self):
        urls = (
            {
                'url': '/hotel/dashboard/',
                'name': 'dashboard',
            },
        )

        for url in urls:
            with self.subTest():
                self.r = self.client.get(url['url'])
                self.assertEqual(302, self.r.status_code)
                self.r = self.client.get(r('hotel:{}'.format(url['name'])))
                self.assertEqual(302, self.r.status_code)
