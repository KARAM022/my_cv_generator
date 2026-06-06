from ..config import Layout


def reset_x(pdf):
    """Set cursor to the default left margin."""
    pdf.set_x(Layout.SECTION_X)


def add_space(pdf, space):
    """Add vertical gap (cm) while keeping left margin."""
    pdf.set_xy(Layout.SECTION_X, pdf.get_y() + space)


def draw_line(pdf, x1, y1, x2=20.0):
    """Draw a thin black horizontal line."""
    pdf.set_draw_color(0, 0, 0)
    pdf.line(x1, y1, x2, y1)