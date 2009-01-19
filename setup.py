from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='MulTweetTwitter',
    version=version,
    description="Twitter plugin for MulTweet",
    long_description="""\
    """,
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='ElevenCraft, Inc.',
    author_email='matt@11craft.com',
    url='',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'MulTweet',
    ],
    entry_points="""
        [multweet]
        twitter = multweettwitter.plugin
    """,
    )
