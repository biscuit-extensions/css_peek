from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.css_peek import setup
from src.css_peek.extension import CSSPeek


class TestCSSPeekExtension:
    def test_extension_setup(self, app_instance) -> None:
        setup(app_instance.api)
        ext = CSSPeek(app_instance.api)
        css = """.card {\n  padding: 1rem;\n}\n.card-header {\n  font-weight: bold;\n}"""
        defs = ext.find_definitions("card", css)
        assert len(defs) == 1
        assert defs[0]["line"] == 1
