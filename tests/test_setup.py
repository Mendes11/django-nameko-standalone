import os
from unittest import TestCase

import django
from django_nameko_standalone import DjangoModels


class SetUpTestCase(TestCase):

    def setUp(self):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_settings")
        os.environ.setdefault("DJANGO_NAMEKO_STANDALONE_SETTINGS_MODULE", "test_settings")
        django_models = DjangoModels()
        django_models.setup()
        django_version = django.VERSION
        self.django_major_version = django_version[0]
        self.django_minor_version = django_version[1]

    def test_set_up(self):
        from django.conf import settings
        self.assertTupleEqual(settings.DJANGO_NAMEKO_STANDALONE_APPS, ("tests",))
        self.assertTupleEqual(settings.INSTALLED_APPS, ("tests",))
        self.assertEqual(settings.SECRET_KEY, '<your_secret_key>')
        expected_databases = {
            'default': {
                'ATOMIC_REQUESTS': False,
                'AUTOCOMMIT': True,
                'CONN_MAX_AGE': 0,
                'ENGINE': 'django.db.backends.dummy',
                'HOST': '',
                'NAME': '',
                'OPTIONS': {},
                'PASSWORD': '',
                'PORT': '',
                'TEST': {
                    'CHARSET': None,
                    'COLLATION': None,
                    'MIGRATE': True,
                    'MIRROR': None,
                    'NAME': None
                },
                'TIME_ZONE': None,
                'USER': ''
            }
        }
        if self.django_major_version >= 4 and self.django_minor_version > 0:
            expected_databases['default']['CONN_HEALTH_CHECKS'] = False
        self.assertDictEqual(settings.DATABASES, expected_databases)
