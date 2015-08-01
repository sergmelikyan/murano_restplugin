import urlparse

import requests


class REST(object):
    @property
    def base_url(self):
        return self._base_url

    @property
    def debug(self):
        return self._debug

    @property
    def with_authentication(self):
        return self._auth

    def initialize(self, _context, base_url, auth=False, debug=True):
        self._base_url = base_url
        self._debug = debug
        self._auth = auth

    def makeRequest(self, url, parse_json=False):
        url = urlparse.urljoin(self.base_url, url)
        r = requests.get(url)
        return r.json() if parse_json else r.text
