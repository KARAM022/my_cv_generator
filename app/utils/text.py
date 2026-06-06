from .layout import reset_x, add_space, draw_line
from ..config import Layout


def text_line(pdf, text="Sample Text", variant="normal", ln=True, align="L"):
    """
    Print a single line with predefined styles.
    Variants: 'title' (Bold 12pt), 'subtitle' (Bold 10pt), 'normal' (Regular 10pt).
    """
    style_map = {
        "title": ("Arial", "B", 12),
        "subtitle": ("Arial", "B", 10),
        "normal": ("Arial", "", 10),
    }
    font, style, size = style_map.get(variant, style_map["normal"])
    pdf.set_font(font, style, size)

    height = 0.5 if variant == "title" else 0.4
    pdf.cell(0, height, text, ln=ln, align=align)


def multi_line_text(pdf, text, font="Arial", style="", size=10, height=0.45):
    """Write multi‑line text using multi_cell."""
    pdf.set_font(font, style, size)
    pdf.multi_cell(0, height, text)


def list_from_text(pdf, text):
    """
    Render bulleted list items.
    Each line of `text` becomes a bullet point; safe width is 17.5 cm.
    """
    lines = text.split("\n")
    usable_width = 17.5
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Bullet
        pdf.set_xy(Layout.SECTION_X + 0.2, pdf.get_y())
        pdf.set_font("DejaVu", "", 10)
        pdf.cell(0.4, 0.45, "•", ln=0, align="C")
        # Text
        pdf.set_font("Arial", "", 10)
        pdf.set_xy(pdf.get_x(), pdf.get_y())
        pdf.multi_cell(usable_width, 0.45, line)
    pdf.set_xy(Layout.SECTION_X, pdf.get_y())


def add_section_title(pdf, title):
    """Print a bold section title with underline and spacing – shared by all sections."""
    text_line(pdf, title, variant="title")
    reset_x(pdf)
    draw_line(pdf, Layout.SECTION_X, pdf.get_y())
    add_space(pdf, Layout.SPACE_AFTER_LINE)