#
# [535] Encode and Decode TinyURL
#
# https://leetcode.com/problems/encode-and-decode-tinyurl/description/
#
# algorithms
# Medium (73.98%)
# Total Accepted:    41.2K
# Total Submissions: 55.7K
# Testcase Example:  '"https://leetcode.com/problems/design-tinyurl"'
#
# Note: This is a companion problem to the System Design problem: Design
# TinyURL.
# 
# TinyURL is a URL shortening service where you enter a URL such as
# https://leetcode.com/problems/design-tinyurl and it returns a short URL such
# as http://tinyurl.com/4e9iAk.
# 
# Design the encode and decode methods for the TinyURL service. There is no
# restriction on how your encode/decode algorithm should work. You just need to
# ensure that a URL can be encoded to a tiny URL and the tiny URL can be
# decoded to the original URL.
#
class Codec:
    def __init__(self):
        self.urlMap = {}
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        shortUrl = 'http://tinyurl.com/' + str(hash(longUrl))
        self.urlMap[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return '' if shortUrl not in self.urlMap else self.urlMap[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
