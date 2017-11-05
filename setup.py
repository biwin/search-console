# -*- coding: utf-8 -*-

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Search Console
# Copyright (C) 2017 Biwin John Joseph


from setuptools import setup, find_packages

setup(
    name='search-console',
    packages=find_packages(),
    version='0.1.1',
    description='A Python Programmable interface to manage search engine consoles.',
    author='Biwin John Joseph',
    author_email='biwinjohn@gmail.com',
    url='https://github.com/biwin/search-console',
    download_url='https://github.com/biwin/search-console',
    keywords=['search console', 'webmaster', 'seo', 'python'],
    classifiers=[],
    include_package_data=True,
    install_requires=[
        'requests',
        'ratelimit',
    ],
)
