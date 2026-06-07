from ..config import Layout
from ..utils.layout import add_space, reset_x
from ..utils.text import text_line, add_section_title


def add_education_section(pdf, data):
    """Full Education section from data."""
    add_section_title(pdf, data["title"])
    entries = data["entries"]
    for i, edu in enumerate(entries):
        reset_x(pdf)
        text_line(pdf, edu["formation"], ln=False)
        text_line(pdf, edu["institution_duration"], ln=True, align="R")
        if i < len(entries) - 1:
            add_space(pdf, Layout.SPACE_BETWEEN_EDUCATION_ENTRIES)