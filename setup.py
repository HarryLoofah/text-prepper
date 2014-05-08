try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A script to manipulate exemplar text for ELA instruction.',
    'author': 'Greg Aitkenhead',
    'url': 'https://github.com/HarryLoofah/text-prepper',
    'download_url': 'https://github.com/HarryLoofah/text-prepper.git',
    'author_email': 'none',
    'version': '0.1.1',
    'install_requires': ['nose'],
    'packages': ['text-prepper'],
    'scripts': [],
    'name': 'TextPrepper'
}

setup(**config)