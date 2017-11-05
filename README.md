# Search Console
A Programmable interface to manage search engine consoles.

## Installation

    pip install search-console


## Documentation

Follow the documentation for respective search engines.

* google : https://developers.google.com/webmaster-tools/search-console-api-original/v3/

### Google Search Console / Google Webmaster Tools


#### Initialization

    from search_console import GoogleSearchConsole

    search = GoogleSearchConsole(api_key='API_KEY', access_token='ACCESS_TOKEN')

#### Usage

| Parameter  | Documented as   | Example  |
|---|---|---|
| `site_url`  | `siteUrl` | `https://www.example.com/` |
|   `feed_path`| `feedPath` | `https://www.example.com/sitemap.xml` |
|  `url` | `url` | `https://www.example.com/pagename` |

Allowed methods.

    search.add_site(site_url)
    search.delete_site(site_url)
    search.get_site(site_url)
    search.list_site(self)
    search.delete_sitemap(site_url, feed_path)
    search.get_sitemap(site_url, feed_path)
    search.list_sitemap(site_url)
    search.submit_sitemap(site_url, feed_path)
    search.url_crawl_error_count(site_url, **kwargs)
    search.get_url_crawl_error_samples(site_url, url, **kwargs)
    search.list_url_crawl_error_sample(site_url, **kwargs)
    search.mark_url_crawl_errors_as_fixed(site_url, url, **kwargs)

## License
This package is released under **GNU GPLV3**

##  Terms of Use
* **Google Search Console**
By using Google Search Console, you agree to the terms and conditions of the following licence(s): 
  * [Google APIs Terms of Service](https://console.developers.google.com/tos?id=universal)
