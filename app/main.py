from pathlib import Path

from fpdf import FPDF


# ----------------------------------------------------------------------
# Paths
# ----------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[1]
FONT_PATH = BASE_DIR / "assets" / "fonts" / "DejaVuSans-Bold.ttf"
IMAGE_PATH = BASE_DIR / "assets" / "images" / "image.png"
OUTPUT_DIR = BASE_DIR / "output"


class CVGenerator:
    """
    A class to generate a CV PDF with a profile image, name, contact details,
    a separator line, and sections for description, skills, experience,
    education, and languages.
    """

    # ------------------------------------------------------------------
    # Layout constants
    # ------------------------------------------------------------------
    # Profile block
    PROFILE_X = 5.4
    PROFILE_Y = 0.1
    PROFILE_MARGIN_AFTER_NAME = 0.3

    # Section placement (after profile)
    SECTION_X = 1.25
    SECTION_Y_START = 4.0

    # Default spacing increments (used by _add_space)
    SPACE_AFTER_LINE = 0.3
    SPACE_AFTER_SUBTITLE = 0.1
    SPACE_BETWEEN_SKILLS_SECTIONS = 0.1
    SPACE_BETWEEN_SECTIONS = 0.4
    SPACE_BETWEEN_EXPERIENCE_COMPANY_AND_TITLE = 0.1
    SPACE_AFTER_EXPERIENCE_TITLE = 0.1
    SPACE_BETWEEN_EXPERIENCE_ENTRIES = 0.3
    SPACE_BETWEEN_EDUCATION_ENTRIES = 0.1

    # ------------------------------------------------------------------
    def __init__(self):
        # Initialise PDF document (portrait, centimetres, A4)
        self.pdf = FPDF("P", "cm", "A4")
        self.pdf.add_page()
        self.pdf.add_font("DejaVu", "", str(FONT_PATH))   # Unicode support
        self.pdf.set_auto_page_break(auto=True, margin=0)

        # Build the CV sections in order
        self._add_image()
        self._add_name()
        self._add_contact()
        self._add_separator_line()
        self._add_description()
        self._add_skills_section()
        self._space_between_sections()
        self._add_experience_section()
        self._space_between_sections()
        self._add_education_section()
        self._space_between_sections()
        self._add_languages_section()

    # ------------------------------------------------------------------
    # Public method
    # ------------------------------------------------------------------
    def save(self, filename: str = "cv.pdf") -> None:
        """Output the PDF to the given filename inside the output directory."""
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        self.pdf.output(str(OUTPUT_DIR / filename))

    # ==================================================================
    # Helper methods for common PDF operations
    # ==================================================================
    def _reset_x(self) -> None:
        """Move cursor to the default left margin (for sections)."""
        self.pdf.set_x(self.SECTION_X)

    def _add_space(self, space: float) -> None:
        """Add a vertical gap (cm) from the current position, keeping the left margin."""
        self.pdf.set_xy(self.SECTION_X, self.pdf.get_y() + space)

    def _text_line(
        self,
        text: str = "Sample Text",
        variant: str = "normal",
        ln: bool = True,
        align: str = "L",
    ) -> None:
        """
        Print a single line of text using predefined font styles.
        Variants: 'title' (Bold 12pt), 'subtitle' (Bold 10pt), 'normal' (Regular 10pt).
        """
        style_map = {
            "title":    ("Arial", "B", 12),
            "subtitle": ("Arial", "B", 10),
            "normal":   ("Arial", "",  10),
        }
        font, style, size = style_map.get(variant, style_map["normal"])
        self.pdf.set_font(font, style, size)

        height = 0.5 if variant == "title" else 0.4
        self.pdf.cell(0, height, text, ln=ln, align=align)

    def _draw_line(self, x1: float, y1: float, x2: float = 20.0) -> None:
        """Draw a thin black horizontal line."""
        self.pdf.set_draw_color(0, 0, 0)
        self.pdf.line(x1, y1, x2, y1)

    def _multi_line_text(self, font: str, style: str, size: int, height: float, text: str) -> None:
        """Write multi‑line text using multi_cell."""
        self.pdf.set_font(font, style, size)
        self.pdf.multi_cell(0, height, text)

    def _list_from_text(self, text: str) -> None:
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
            self.pdf.set_xy(self.SECTION_X + 0.2, self.pdf.get_y())
            self.pdf.set_font("DejaVu", "", 10)
            self.pdf.cell(0.4, 0.45, "•", ln=0, align="C")

            # Text
            self.pdf.set_font("Arial", "", 10)
            self.pdf.set_xy(self.pdf.get_x(), self.pdf.get_y())
            self.pdf.multi_cell(usable_width, 0.45, line)

        self.pdf.set_xy(self.SECTION_X, self.pdf.get_y())

    # ------------------------------------------------------------------
    # Specific spacing methods (thin wrappers around _add_space)
    # ------------------------------------------------------------------
    def _space_after_line(self) -> None:
        self._add_space(self.SPACE_AFTER_LINE)

    def _space_after_subtitle(self) -> None:
        self._add_space(self.SPACE_AFTER_SUBTITLE)

    def _space_between_skills_sections(self) -> None:
        self._add_space(self.SPACE_BETWEEN_SKILLS_SECTIONS)

    def _space_between_sections(self) -> None:
        self._add_space(self.SPACE_BETWEEN_SECTIONS)

    def _space_between_experience_company_and_title(self) -> None:
        self._add_space(self.SPACE_BETWEEN_EXPERIENCE_COMPANY_AND_TITLE)

    def _space_after_experience_title(self) -> None:
        self._add_space(self.SPACE_AFTER_EXPERIENCE_TITLE)

    def _space_between_experience_entries(self) -> None:
        self._add_space(self.SPACE_BETWEEN_EXPERIENCE_ENTRIES)

    def _space_between_education_entries(self) -> None:
        self._add_space(self.SPACE_BETWEEN_EDUCATION_ENTRIES)

    # ==================================================================
    # CV building blocks
    # ==================================================================
    def _add_image(self) -> None:
        """Insert the profile picture at a fixed position."""
        self.pdf.image(
            str(IMAGE_PATH),
            x=1.25,
            y=0.6,
            w=3,
            h=3,
        )
        # Set initial text cursor for the profile block
        self.pdf.set_xy(self.PROFILE_X, self.PROFILE_Y)

    def _add_name(self) -> None:
        """Add the full name and adjust Y for the next line."""
        self.pdf.set_font("Arial", "", 32)
        self.pdf.cell(0, 1.34, "Ouaifik Karam", ln=True)
        # Lift cursor slightly to reduce gap before contact details
        self.pdf.set_xy(self.PROFILE_X, self.pdf.get_y() - self.PROFILE_MARGIN_AFTER_NAME)

    def _add_contact(self) -> None:
        """Add contact information on one line."""
        self.pdf.set_font("Arial", "", 14)
        self.pdf.cell(0, 1, "Casablanca | +212 608-310554 | ouafik0karam@gmail.com", ln=True)

    def _add_separator_line(self) -> None:
        """Draw a black horizontal line below the contact info."""
        y_line = self.pdf.get_y() - 0.1
        self._draw_line(self.PROFILE_X, y_line)
        self.pdf.set_xy(self.PROFILE_X, self.pdf.get_y())

    def _add_description(self) -> None:
        """Multi‑line professional description."""
        desc = (
            "Fullstack Developer & Data Engineer, specialise en developpement d'applications web "
            "et en gestion de donnees. Competent en front-end/back-end et en ingenierie des donnees, "
            "je transforme les besoins metiers en solutions performantes. Rigoureux et motive, "
            "je suis ouvert a de nouvelles opportunites."
        )
        self._multi_line_text("Arial", "", 10, 0.45, desc)
        # After description, move to the standard section start position
        self.pdf.set_xy(self.SECTION_X, self.SECTION_Y_START)

    # ------------------------------------------------------------------
    # Section title with underline
    # ------------------------------------------------------------------
    def _add_section_title(self, title: str) -> None:
        """Print a bold section title and underline it."""
        self._text_line(title, variant="title")
        self._reset_x()
        self._draw_line(self.SECTION_X, self.pdf.get_y())
        self._space_after_line()

    # ------------------------------------------------------------------
    # Skills section
    # ------------------------------------------------------------------
    def _add_skills_section(self) -> None:
        self._add_section_title("Compétences Techniques")
        self._add_skills_subsection(
            "Développement Fullstack",
            (
                "Front-End : HTML, CSS, JavaScript, React.js, Bootstrap, JQuery, Responsive/Mobile-first design, Optimisation web\n"
                "Back-End : PHP, Python, Laravel, Node.js, Express.js\n"
                "Mobile : React Native, Flutter\n"
                "Bases de données : MySQL, MongoDB\n"
                "DevOps & Outils : Git, GitHub, GitLab, Nginx, Linux, Shell scripting\n"
                "Méthodologies : Agile (Scrum)\n"
                "Sécurité : Sécurité des applications web, déploiement & maintenance serveurs"
            ),
        )
        self._space_between_skills_sections()
        self._add_skills_subsection(
            "Ingénierie des Données",
            (
                "Data Mining & Statistical Analysis\n"
                "Database Management: SQL & NoSQL (MySQL, MongoDB)\n"
                "Data Warehousing & Visualization: Power BI, Python (Pandas, Matplotlib, Seaborn)\n"
                "Big Data Fundamentals: data acquisition, processing & quality management\n"
                "Data Governance: data quality assurance & security"
            ),
        )

    def _add_skills_subsection(self, subtitle: str, content: str) -> None:
        """Print a skills category subtitle followed by bullet points."""
        self._reset_x()
        self._text_line(subtitle, variant="subtitle")
        self._space_after_subtitle()
        self._list_from_text(content)

    # ------------------------------------------------------------------
    # Experience section
    # ------------------------------------------------------------------
    def _add_experience_section(self) -> None:
        self._add_section_title("Expérience Professionnelle")
        experiences = [
            {
                "company": "GivenX",
                "duration": "11/2025 - 03/2026",
                "title": "Développeur & Tech Lead",
                "tasks": (
                    "Conception, développement et déploiement d'applications web et mobiles.\n"
                    "Pilotage technique des projets : encadrement de l'équipe, répartition des tâches, revue de code et garantie de la qualité des livrables."
                ),
            },
            {
                "company": "ClickDigital",
                "duration": "10/2025 - 02/2026",
                "title": "Développeur Web & Mobile",
                "tasks": (
                    "Développement de Flousafe (React.js, Next.js, Flutter) avec déploiement, sécurité et  optimisation des performances.\n"
                    "Conception d'interfaces responsives et modernes axées sur l'expérience utilisateur."
                ),
            },
            {
                "company": "23Digit",
                "duration": "01/2025 - 06/2025",
                "title": "Développeur Full Stack (Stage)",
                "tasks": (
                    "Développement de solutions web et mobiles de gestion de caisse (Laravel, Node.js, React,React Native, Flutter).\n"
                    "Déploiement et maintenance des applications sur serveurs pour l'ensemble des projets livrés."
                ),
            },
            {
                "company": "LMS Organisation & RH",
                "duration": "08/2024 - 10/2024",
                "title": "Développeur Intégration Systèmes (Stage)",
                "tasks": (
                    "Conception et intégration d'APIs et solutions middleware.\n"
                    "Documentation technique et optimisation des performances systèmes."
                ),
            },
            {
                "company": "Groupe Scolaire Khawater",
                "duration": "05/2024",
                "title": "Développeur Systèmes Informatiques (Stage)",
                "tasks": (
                    "Migration vers une architecture microservices.\n"
                    "Gestion de l'infrastructure web et assistance technique."
                ),
            },
        ]

        for i, exp in enumerate(experiences):
            self._add_one_experience(exp)
            if i < len(experiences) - 1:
                self._space_between_experience_entries()

    def _add_one_experience(self, exp: dict) -> None:
        """Render a single experience entry: company, duration, title, tasks."""
        self._reset_x()
        # Company name
        self._text_line(exp["company"], variant="subtitle", ln=False)
        # Duration (right aligned on the same line)
        self._text_line(exp["duration"], variant="subtitle", align="R")

        self._space_between_experience_company_and_title()

        # Title
        self._reset_x()
        self._text_line(exp["title"], variant="normal")

        self._space_after_experience_title()

        # Tasks as bullet list
        self._list_from_text(exp["tasks"])

    # ------------------------------------------------------------------
    # Education section
    # ------------------------------------------------------------------
    def _add_education_section(self) -> None:
        self._add_section_title("Formation")
        entries = [
            {
                "formation": "Licence Professionnelle d'Université en Ingénierie des Données",
                "institution-duration": "ENSAM - 2025",
            },
            {
                "formation": "Certificat de Génie Logiciel",
                "institution-duration": "ALX - 2024",
            },
            {
                "formation": "Diplôme de Technicien Spécialisé en Développement Digital Web Full Stack",
                "institution-duration": "CFPMS(OFPPT) - 2024",
            },
            {
                "formation": "Baccalauréat / Sciences de la Vie et de la Terre",
                "institution-duration": "Lycée Moulay Youssef - 2022",
            },
        ]

        for i, edu in enumerate(entries):
            self._reset_x()
            self._text_line(edu["formation"], ln=False)
            self._text_line(edu["institution-duration"], ln=True, align="R")
            if i < len(entries) - 1:
                self._space_between_education_entries()

    # ------------------------------------------------------------------
    # Languages section
    # ------------------------------------------------------------------
    def _add_languages_section(self) -> None:
        self._reset_x()
        self._add_section_title("Langues")
        self._text_line(
            "Arabe : Langue maternelle | Anglais : Intermédiaire | Français : Opérationnel"
        )


# --------------------------------------------------------------------------
if __name__ == "__main__":
    cv = CVGenerator()
    cv.save("Ouafik_Karam1.pdf")