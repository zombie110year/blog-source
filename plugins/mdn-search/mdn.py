# -*- coding: utf-8 -*-
"""mdn role for reStructuredText."""

from docutils import nodes
from docutils.parsers.rst import roles
from docutils.parsers.rst.states import Inliner
from nikola.plugin_categories import RestExtension
from typing import *


class Plugin(RestExtension):
    """Plugin for reST mdn role"""

    name = "rest_mdn"

    def set_site(self, site):
        """Set Nikola site."""
        self.site = site
        roles.register_canonical_role('mdn', mozilla_developer_network)
        return super(Plugin, self).set_site(site)


def mozilla_developer_network(name: str,
                              rawtext: str,
                              text: str,
                              lineno: int,
                              inliner: Inliner,
                              options: dict = {},
                              content: List[str] = []):
    """reST extension for replace :mdn:`HelloWorld` to
    <a href="https://developer.mozilla.org/zh-CN/search?q=HelloWorld">HelloWorld</a>
    """
    query_word = text
    url = f"https://developer.mozilla.org/search?q={query_word}"
    return [nodes.reference(rawtext, query_word, refuri=url, **options)], []
