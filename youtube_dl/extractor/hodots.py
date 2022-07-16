from __future__ import unicode_literals

from .common import InfoExtractor


class hodotsVideoIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?hodots\.com/post\?p=(?P<id>[0-9A-Za-z]{15}+)'
    _TEST = {
        'url': 'https://hodots.com/post?p=swcaldrrdhritjz',
        'md5': 'This doesnt have MD5 so yeah',
        'info_dict': {
            'id': 'swcaldrrdhritjz',
            'ext': 'mp4',
            'title': 'Jo (edit)',
            'thumbnail': r're:^https?://.*\.png$',
        }
    }

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)
        title = self._html_search_regex(r'<div[^>]+id="posttexts"[^>]+class="posttitle"[^>]+style="padding-top:10px;"[^>]*>([^<]+<span[^>]+class=""[^>]*>([^<]+)<(.+?)', webpage, 'title')
        return {
            'id': video_id,
            'title': title,
            'description': self._og_search_description(webpage),
            'uploader': self._search_regex(r'<div[^>]+id="postauthortext"[^>]*>([^<]+)<', webpage, 'uploader')
        }
