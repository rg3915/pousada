from django.shortcuts import resolve_url as r
from django.test import TestCase
from django.test.client import Client


class UrlTest(TestCase):

    def test_urls(self):
        urls = (
            {
                'url': '/',
                'name': 'home',
            },
            {
                'url': '/contato/',
                'name': 'contato',
            },
            {
                'url': '/servicos/',
                'name': 'servicos',
            },

        )

        for url in urls:
            with self.subTest():
                self.r = self.client.get(url['url'])
                self.assertEqual(200, self.r.status_code)
                self.r = self.client.get(r('core:{}'.format(url['name'])))
                self.assertEqual(200, self.r.status_code)

    def test_urls_302(self):
        urls = (
            {
                'url': '/contato/add/',
                'name': 'contato_add',
            },
        )

        for url in urls:
            with self.subTest():
                self.r = self.client.get(url['url'])
                self.assertEqual(302, self.r.status_code)
                self.r = self.client.get(r('core:{}'.format(url['name'])))
                self.assertEqual(302, self.r.status_code)
