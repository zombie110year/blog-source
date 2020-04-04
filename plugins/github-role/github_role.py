# -*- coding: utf-8 -*-
"""github role for reStructuredText."""

import re
from docutils import nodes
from docutils.parsers.rst import roles
from docutils.parsers.rst.states import Inliner
from nikola.plugin_categories import RestExtension
from typing import *


class Plugin(RestExtension):
    """Plugin for reST github role"""

    name = "rest_github"

    def set_site(self, site):
        """Set Nikola site."""
        self.site = site
        roles.register_canonical_role('github', github_repository)
        return super(Plugin, self).set_site(site)


def github_repository(name: str,
                      rawtext: str,
                      text: str,
                      lineno: int,
                      inliner: Inliner,
                      options: dict = {},
                      content: List[str] = []):
    """reST extension for replace :github:`zombie110year/blog-source` to
    <a href="https://github.com/zombie110year/blog-source">zombie110year/blog-source | GitHub</a>
    """
    owner_repo = re.search(r"(?P<owner>\S+)/(?P<repo>\S+)", text)
    if owner_repo is not None:
        owner = owner_repo["owner"]
        repo = owner_repo["repo"]
        url = f"https://github.com/{owner}/{repo}"
        return [nodes.reference(rawtext, f"{owner}/{repo} | GitHub", refuri=url, **options)], []
    else:
        return [], [f"Error: input cannot be refered to a GitHub repository."]
