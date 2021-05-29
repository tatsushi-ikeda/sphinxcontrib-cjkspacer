# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

try:
    with open('README.md') as f:
        readme_md = f.read()
except IOError:
    readme_md = ''

def _requires_from_file(filename):
    return open(filename).read().splitlines()

setup(
    name='sphinxcontrib-cjkspacer',
    version='0.2.1',
    url='https://github.com/tatsushi-ikeda/sphinxcontrib-cjkspacer',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-cjkspacer',
    license='MIT',
    author='tatsushi-ikeda',
    author_email='ikeda.tatsushi.37u@kyoto-u.jp',
    description='Sphinx "cjkspacer" extension',
    long_description=readme_md,
    long_description_content_type='text/markdown',
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=_requires_from_file('requirements.txt'),
    namespace_packages=['sphinxcontrib'],
)
