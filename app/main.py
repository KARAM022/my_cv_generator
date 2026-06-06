import json
from fpdf import FPDF

from .config import FONT_PATH, OUTPUT_DIR, DATA_PATH, Layout
from .sections import profile, skills, experience, education, languages
from .utils.layout import add_space


class CVGenerator:
    """
    Orchestrates the creation of a CV PDF.
    Loads content from a JSON file and draws each section.
    """

    def __init__(self):
        self.pdf = FPDF("P", "cm", "A4")
        self.pdf.add_page()
        self.pdf.add_font("DejaVu", "", str(FONT_PATH))
        self.pdf.set_auto_page_break(auto=True, margin=0)

        # Load content data
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            self.data = json.load(f)

        # Build the CV in order
        # Profile includes image, name, contact, separator, and description
        profile.add_profile(self.pdf, self.data)

        skills.add_skills_section(self.pdf, self.data["skills"])
        add_space(self.pdf, Layout.SPACE_BETWEEN_SECTIONS)

        experience.add_experience_section(self.pdf, self.data["experience"])
        add_space(self.pdf, Layout.SPACE_BETWEEN_SECTIONS)

        education.add_education_section(self.pdf, self.data["education"])
        add_space(self.pdf, Layout.SPACE_BETWEEN_SECTIONS)

        languages.add_languages_section(self.pdf, self.data["languages"])

    def save(self, filename=None):
        """
        Output the PDF to the output directory.
        If no filename is given, uses the name from the data (pdf_filename).
        Falls back to 'cv.pdf' if not provided.
        """
        if filename is None:
            filename = self.data.get("pdf_filename", "cv.pdf")
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        self.pdf.output(str(OUTPUT_DIR / filename))