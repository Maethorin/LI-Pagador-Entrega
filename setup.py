# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='li-pagador-retirada',
    version='0.0.1',
    url='https://github.com/lojaintegrada/LI-Pagador-Entrega',
    license='MIT',
    description=u'Meio de pagamento usado na retirada em loja',
    author=u'Loja Integrada',
    author_email='suporte@lojaintegrada.com.br',
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet",
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    package_data={'pagador_retirada': ['extensao/templates/*']},
    install_requires=['distribute', 'li-pagador'],
)