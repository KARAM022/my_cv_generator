from ..config import Layout
from ..utils.layout import reset_x
from ..utils.text import text_line, add_section_title


def add_languages_section(pdf, data):
    """Full Languages section from data."""
    reset_x(pdf)
    add_section_title(pdf, data["title"])
    text_line(pdf, data["content"])