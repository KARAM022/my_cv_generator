from ..config import IMAGE_PATH, Layout
from ..utils.layout import draw_line
from ..utils.text import multi_line_text


def add_profile(pdf, data):
    """Insert image, name, contact, separator line, and description."""
    # Profile image
    pdf.image(str(IMAGE_PATH), x=1.25, y=0.6, w=3, h=3)
    pdf.set_xy(Layout.PROFILE_X, Layout.PROFILE_Y)

    # Name
    pdf.set_font("Arial", "", 32)
    pdf.cell(0, 1.34, data["name"], ln=True)
    pdf.set_xy(Layout.PROFILE_X, pdf.get_y() - Layout.PROFILE_MARGIN_AFTER_NAME)

    # Contact
    pdf.set_font("Arial", "", 14)
    pdf.cell(0, 1, data["contact"], ln=True)

    # Separator line
    y_line = pdf.get_y() - 0.1
    draw_line(pdf, Layout.PROFILE_X, y_line)
    pdf.set_xy(Layout.PROFILE_X, pdf.get_y())

    # Description
    multi_line_text(pdf, data["description"], font="Arial", style="", size=10, height=0.45)
    pdf.set_xy(Layout.SECTION_X, Layout.SECTION_Y_START)