# -*- coding: utf-8 -*-
"""github role for reStructuredText."""

import re
import requests as r
from dataclasses import dataclass
from functools import lru_cache

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
        info = check_github_repo(owner, repo)
        return [nodes.reference(rawtext, info.title, refuri=info.url, **options)], []
    else:
        return [], [f"Error: input cannot be refered to a GitHub repository."]


@dataclass
class GithubInfo:
    owner: str
    repo: str

    @property
    def url(self):
        return f"https://github.com/{self.owner}/{self.repo}"

    @property
    def title(self):
        return f"GitHub - {self.owner}/{self.repo}"


@lru_cache
def check_github_repo(owner: str, repo: str) -> GithubInfo:
    # todo: get description
    info = GithubInfo(owner=owner, repo=repo)
    return info
