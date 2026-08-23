from __future__ import annotations

import typing

from biscuit.extensions import Extension

if typing.TYPE_CHECKING:
    from biscuit.api import ExtensionsAPI


import re

class CSSPeek(Extension):
    """Jump directly to CSS selector definitions from HTML classes and IDs."""

    def __init__(self, api: ExtensionsAPI) -> None:
        super().__init__(api)
        self.api = api
        self.api.logger.info("CSS Peek extension initialised.")

    def find_definitions(self, selector: str, css_text: str) -> list[dict]:
        target = f".{selector}" if not selector.startswith((".", "#")) else selector
        results = []
        for line_no, line in enumerate(css_text.splitlines(), start=1):
            if re.search(re.escape(target) + r"(?:\s*[,{]|\s*$)", line):
                results.append({"line": line_no, "selector": target, "content": line.strip()})
        return results

    def install(self) -> None:
        self.api.logger.info("CSS Peek extension installed.")
