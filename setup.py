#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    author='ParthKolekar',
    author_email='parth.kolekar@students.iiit.ac.in',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
    ],
    description='CAS 1.0/2.0 authentication backend for Django',
    keywords='django cas cas2 authentication middleware backend',
    license='MIT',
    long_description="""
..  Forked from the original source https://bitbucket.org/cpcc/django-cas
..  This attempts to drop compablity for older versions of Django and CAS, and build upon the latest alone.
..  Continued versioning from the base.
.. _CAS: http://www.ja-sig.org/products/cas/
.. _Django: http://www.djangoproject.com/
""",
    name='django_cas',
    packages=['django_cas'],
    url='https://github.com/ParthKolekar/django-cas',
    version='2.1.1',
)
