from ..config import Layout
from ..utils.layout import add_space, reset_x
from ..utils.text import text_line, list_from_text, add_section_title


def _add_subsection(pdf, subtitle, content):
    """Print a skills category subtitle followed by bullet points."""
    reset_x(pdf)
    text_line(pdf, subtitle, variant="subtitle")
    add_space(pdf, Layout.SPACE_AFTER_SUBTITLE)
    list_from_text(pdf, content)


def add_skills_section(pdf, data):
    """Full Skills section from data."""
    add_section_title(pdf, data["title"])
    subsections = data["subsections"]
    for i, sub in enumerate(subsections):
        _add_subsection(pdf, sub["subtitle"], sub["content"])
        if i < len(subsections) - 1:
            add_space(pdf, Layout.SPACE_BETWEEN_SKILLS_SECTIONS)