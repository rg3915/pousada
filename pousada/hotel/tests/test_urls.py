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

    def test_urls_pessoas(self):
        urls = (
            {
                'url': '/hotel/pessoas/pessoas/',
                'name': 'pessoas',
            },
            {
                'url': '/hotel/pessoas/pessoas/add/',
                'name': 'pessoas_add',
            },
        )

        for url in urls:
            with self.subTest():
                self.r = self.client.get(url['url'])
                self.assertEqual(302, self.r.status_code)
                self.r = self.client.get(r('hotel:{}'.format(url['name'])))
                self.assertEqual(302, self.r.status_code)

    def test_urls_quartos(self):
        urls = (
            {
                'url': '/hotel/quartos/quartos/',
                'name': 'quartos',
            },
        )

        for url in urls:
            with self.subTest():
                self.r = self.client.get(url['url'])
                self.assertEqual(302, self.r.status_code)
                self.r = self.client.get(r('hotel:{}'.format(url['name'])))
                self.assertEqual(302, self.r.status_code)

    def test_urls_rotativos(self):
        urls = (
            {
                'url': '/hotel/rotativos/rotativos/',
                'name': 'rotativos',
            },
        )

        for url in urls:
            with self.subTest():
                self.r = self.client.get(url['url'])
                self.assertEqual(302, self.r.status_code)
                self.r = self.client.get(r('hotel:{}'.format(url['name'])))
                self.assertEqual(302, self.r.status_code)

    def test_urls_mensalistas(self):
        urls = (
            {
                'url': '/hotel/mensalistas/mensalistas/',
                'name': 'mensalistas',
            },
        )

        for url in urls:
            with self.subTest():
                self.r = self.client.get(url['url'])
                self.assertEqual(302, self.r.status_code)
                self.r = self.client.get(r('hotel:{}'.format(url['name'])))
                self.assertEqual(302, self.r.status_code)
