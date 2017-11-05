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
#
# Search Console
# Copyright (C) 2017 Biwin John Joseph


from __future__ import with_statement

import requests
from ratelimit import *

try:
    import urllib.parse as urllib
except ImportError:
    import urllib


class GoogleSearchConsole(object):
    """
    Wrapper to interact with Google Search Console API
    https://developers.google.com/webmaster-tools/search-console-api-original/v3/
    """

    def __init__(self, api_key, access_token):
        """ initialize Google Search Console API"""
        self.api_key = api_key
        self.headers = {
            'authorization': 'Bearer %s' % access_token,
            'referer': 'https://developers.google.com'
        }
        self.endpoint = 'https://www.googleapis.com/webmasters/v3/'

    @rate_limited(3)
    def make_api_call(self, url, method='GET'):
        """ makes an api call to the endpoint """
        print method, url
        if method == 'GET':
            return requests.get(url, headers=self.headers)
        elif method == 'PUT':
            return requests.put(url, headers=self.headers)
        elif method == 'DELETE':
            return requests.delete(url, headers=self.headers)
        elif method == 'PUT':
            return requests.put(url, headers=self.headers)

    def add_site(self, site_url):
        """ Adds a site to the set of the user's sites in Search Console. """
        endpoint = self.endpoint + 'sites/%s?key=%s' \
                                   % (urllib.quote_plus(site_url), self.api_key)
        return self.make_api_call(endpoint, method='PUT')

    def delete_site(self, site_url):
        """ Removes a site from the set of the user's Search Console sites. """
        endpoint = self.endpoint + 'sites/%s?key=%s' \
                                   % (urllib.quote_plus(site_url), self.api_key)
        return self.make_api_call(endpoint, method='DELETE')

    def get_site(self, site_url):
        """ Retrieves information about specific site."""
        endpoint = self.endpoint + 'sites/%s?key=%s' \
                                   % (urllib.quote_plus(site_url), self.api_key)
        return self.make_api_call(endpoint)

    def list_site(self):
        """Lists the user's Search Console sites."""
        endpoint = self.endpoint + 'sites?key=%s' \
                                   % self.api_key
        return self.make_api_call(endpoint)

    def delete_sitemap(self, site_url, feed_path):
        """ Deletes a sitemap from this site."""
        endpoint = self.endpoint + 'sites/%s/sitemaps/%s?key=%s' \
                                   % (urllib.quote_plus(site_url), urllib.quote_plus(feed_path), self.api_key)
        return self.make_api_call(endpoint, method='DELETE')

    def get_sitemap(self, site_url, feed_path):
        """ Retrieves information about a specific sitemap."""
        endpoint = self.endpoint + 'sites/%s/sitemaps/%s?key=%s' \
                                   % (urllib.quote_plus(site_url), urllib.quote_plus(feed_path), self.api_key)
        return self.make_api_call(endpoint)

    def list_sitemap(self, site_url):
        """ Lists the sitemaps-entries submitted for this site,
        or included in the sitemap index file (if sitemapIndex is specified in the request)."""
        endpoint = self.endpoint + 'sites/%s/sitemaps?key=%s' \
                                   % (urllib.quote_plus(site_url), self.api_key)
        return self.make_api_call(endpoint)

    def submit_sitemap(self, site_url, feed_path):
        """ Submits a sitemap for a site."""
        endpoint = self.endpoint + 'sites/%s/sitemaps/%s?key=%s' \
                                   % (urllib.quote_plus(site_url), urllib.quote_plus(feed_path), self.api_key)
        return self.make_api_call(endpoint, method='PUT')

    def url_crawl_error_count(self, site_url, **kwargs):
        """
        Retrieves a time series of the number of URL crawl errors per error category and platform.

        kwargs:

            category: <string>   The crawl error category.
                                For example: serverError. If not specified, returns results for all categories.

                                Acceptable values
                                 "authPermissions" | "flashContent"| "manyToOneRedirect"| "notFollowed"|
                                 "notFound"| "other"| "roboted"| "serverError"| "soft404"

            latestCountsOnly: <boolean>	If true, returns only the latest crawl error counts.
                                (Default: true)

            platform: string    The user agent type (platform) that made the request.
                                For example: web. If not specified, returns results for all platforms.

                                Acceptable values:
                                    "mobile" | "smartphoneOnly" | "web"
        """
        endpoint = self.endpoint + "sites/%s/urlCrawlErrorsCounts/query?key=%s" \
                                   % (site_url, self.api_key)
        if kwargs:
            query_string = urllib.urlencode(kwargs)
            endpoint = endpoint + "&%s" % query_string

        return self.make_api_call(endpoint)

    def get_url_crawl_error_samples(self, site_url, url, **kwargs):
        """ Retrieves details about crawl errors for a site's sample URL. """
        endpoint = self.endpoint + "sites/%s/urlCrawlErrorsSamples/%s?key=%s" \
                                   % (urllib.quote_plus(site_url), url, self.api_key)
        if kwargs:
            query_string = urllib.urlencode(kwargs)
            endpoint = endpoint + "&%s" % query_string
        return self.make_api_call(endpoint)

    def list_url_crawl_error_sample(self, site_url, **kwargs):
        """ Lists a site's sample URLs for the specified crawl error category and platform.  """
        endpoint = self.endpoint + "sites/%s/urlCrawlErrorsSamples?key=%s" \
                                   % (urllib.quote_plus(site_url), self.api_key)
        if kwargs:
            query_string = urllib.urlencode(kwargs)
            endpoint = endpoint + "&%s" % query_string
        return self.make_api_call(endpoint)

    def mark_url_crawl_errors_as_fixed(self, site_url, url, **kwargs):
        """" Marks the provided site's sample URL as fixed, and removes it from the samples list. """
        endpoint = self.endpoint + "sites/%s/urlCrawlErrorsSamples/%s?key=%s" \
                                   % (urllib.quote_plus(site_url), url, self.api_key)
        if kwargs:
            query_string = urllib.urlencode(kwargs)
            endpoint = endpoint + "&%s" % query_string
        return self.make_api_call(endpoint, method='DELETE')
