from ..config import Layout
from ..utils.layout import add_space, reset_x
from ..utils.text import text_line, list_from_text, add_section_title


def add_experience_section(pdf, data):
    """Full Experience section from data."""
    add_section_title(pdf, data["title"])
    entries = data["entries"]
    for i, exp in enumerate(entries):
        reset_x(pdf)
        # Company and duration on same line
        text_line(pdf, exp["company"], variant="subtitle", ln=False)
        text_line(pdf, exp["duration"], variant="subtitle", align="R")
        add_space(pdf, Layout.SPACE_BETWEEN_EXPERIENCE_COMPANY_AND_TITLE)

        # Title
        reset_x(pdf)
        text_line(pdf, exp["title"], variant="normal")
        add_space(pdf, Layout.SPACE_AFTER_EXPERIENCE_TITLE)

        # Tasks as bullet list
        list_from_text(pdf, exp["tasks"])

        if i < len(entries) - 1:
            add_space(pdf, Layout.SPACE_BETWEEN_EXPERIENCE_ENTRIES)