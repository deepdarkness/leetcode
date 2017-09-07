import hashlib


class Codec(object):
    """
    https://leetcode.com/problems/design-tinyurl
    http://tinyurl.com/4e9iAk
    """

    def __init__(self):
        self.md5lib = hashlib.md5()
        self.now_num = 0
        self.short_long_url = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        short_url_prefix = 'http://tinyurl.com/'
        short_url_suffix = hashlib.md5(longUrl.encode('utf-8')).hexdigest()[:6]
        while short_url_suffix in self.short_long_url:
            short_url_suffix = hex(int(short_url_suffix, 16) + 1)[2:]
        self.short_long_url[short_url_suffix] = longUrl
        return short_url_prefix + short_url_suffix

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        short_url_suffix = shortUrl[shortUrl.rfind('/') + 1:]
        return self.short_long_url[short_url_suffix] if short_url_suffix in self.short_long_url else None


url = 'https://leetcode.com/problems/design-tinyurl'
codec = Codec()
print(codec.decode(codec.encode(url)))
