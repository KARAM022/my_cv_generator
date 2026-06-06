from fpdf import FPDF

class CVGenerator:
    """
    A class to generate a CV PDF with a profile image, name, contact details,
    a separator line, and a description.
    """

    def __init__(self):
        # Initialize PDF document (portrait, centimeters, A4)
        self.pdf = FPDF("P", "cm", "A4")
        self.pdf.add_page()
        self.pdf.add_font("DejaVu", "", "DejaVuSans-Bold.ttf")  # Load DejaVu for Unicode support
        self.pdf.set_auto_page_break(auto=True, margin=0)

        # Layout constants (same as original code)
        self.profile_x = 5.4      # X coordinate for text block
        self.profile_y = 0.1      # Initial Y coordinate for text block
        self.default_space = 0.3  # Vertical gap adjustment

        self.default_y = 4  # Y coordinate for sections after profile
        self.default_x = 1.25  # X coordinate for sections after profile
        self.default_space_after_line = 0.3  # Space after separator line
        self.default_space_after_subtitle = 0.1  # Space after section subtitles
        self.default_space_between_skills_sections = 0.1  # Space between skills subsections
        self.default_space_between_sections = 0.4  # Space between main sections (skills, experience, education, languages)
        self.default_space_between_experience_company_and_title = 0.1  # Space between company/duration line and title in experience section
        self.default_space_after_experience_title = 0.1  # Space after experience title before tasks
        self.default_space_between_experience_entries = 0.3  # Space between experience entries
        self.default_space_between_education_entries = 0.1  # Space between education entries

        # Build the CV by calling each component in order
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

    # ----------------------------------------------------------------------
    # Private methods for style and layout (e.g., adding images, setting fonts, drawing lines)
    # ----------------------------------------------------------------------
    def _text_single_line(self, variant="normal", text="Sample Text", ln=True, align="L"):
        """Helper method to add a single line of text with consistent styling."""
        self.pdf.set_font(
            "Arial",
            "" if variant == "normal" else "B",
            12 if variant == "title" else 10
        )
        self.pdf.cell(
            0,
            0.5 if variant == "title" else 0.4,
            text,
            ln=ln,
            align=align
        )

    def _left_align(self):
        """Set left alignment for the current line."""
        self.pdf.set_x(self.default_x)

    def _space_after_line(self, space=None):
        """Add vertical space after the current line."""
        if space is None:
            space = self.default_space_after_line
        self.pdf.set_xy(self.default_x, self.pdf.get_y() + space)

    def _space_after_subtitle(self, space=None):
        """Add vertical space after a subtitle."""
        if space is None:
            space = self.default_space_after_subtitle
        self.pdf.set_xy(self.default_x, self.pdf.get_y() + space)

    def _space_between_skills_sections(self, space=None):
        """Add vertical space between skills subsections."""
        if space is None:
            space = self.default_space_between_skills_sections
        self.pdf.set_xy(self.default_x, self.pdf.get_y() + space)

    def _space_between_sections(self, space=None):
        """Add vertical space between main sections (skills, experience, education, languages)."""
        if space is None:
            space = self.default_space_between_sections
        self.pdf.set_xy(self.default_x, self.pdf.get_y() + space)
    
    def _space_between_experience_company_and_title(self, space=None):
        """Add vertical space between company/duration line and title in experience section."""
        if space is None:
            space = self.default_space_between_experience_company_and_title
        self.pdf.set_xy(self.default_x, self.pdf.get_y() + space)
    
    def _space_after_experience_title(self, space=None):
        """Add vertical space after experience title before tasks."""
        if space is None:
            space = self.default_space_after_experience_title
        self.pdf.set_xy(self.default_x, self.pdf.get_y() + space)
    
    def _space_between_experience_entries(self, space=None):
        """Add vertical space between experience entries."""
        if space is None:
            space = self.default_space_between_experience_entries
        self.pdf.set_xy(self.default_x, self.pdf.get_y() + space)
    
    def _space_between_education_entries(self, space=None):
        """Add vertical space between education entries."""
        if space is None:
            space = self.default_space_between_education_entries
        self.pdf.set_xy(self.default_x, self.pdf.get_y() + space)

    
    # ----------------------------------------------------------------------
    # Private methods for each part of the CV
    # ----------------------------------------------------------------------
    def _add_image(self):
        """Insert the profile image at fixed coordinates."""
        img_info = {
            "path": "image.png",
            "width": 3,
            "height": 3,
            "x": 1.25,
            "y": 0.6
        }
        self.pdf.image(
            img_info["path"],
            x=img_info["x"],
            y=img_info["y"],
            h=img_info["height"],
            w=img_info["width"]
        )

        # Set initial position for text after adding the image
        self.pdf.set_xy(self.profile_x, self.profile_y)

    def _add_name(self):
        """Add the full name and adjust vertical position for the next element."""
        name_info = {
            "font": "Arial",
            "style": "",
            "size": 32,
            "width": 0,
            "height": 1.34,
            "ln": True,
            "name": "Ouaifik Karam"
        }
        self.pdf.set_font(name_info["font"], name_info["style"], name_info["size"])
        self.pdf.cell(name_info["width"], name_info["height"], name_info["name"], ln=name_info["ln"])

        # Move cursor slightly upward to reduce gap before contact details
        self.pdf.set_xy(self.profile_x, self.pdf.get_y() - self.default_space)

    def _add_contact(self):
        """Add the contact information line."""
        contact_info = {
            "font": "Arial",
            "style": "",
            "size": 14,
            "width": 0,
            "height": 1,
            "ln": True,
            "contact": "Casablanca | +212 608-310554 | ouafik0karam@gmail.com"
        }
        self.pdf.set_font(contact_info["font"], contact_info["style"], contact_info["size"])
        self.pdf.cell(contact_info["width"], contact_info["height"], contact_info["contact"], ln=contact_info["ln"])

    def _add_separator_line(self):
        """Draw a black horizontal line below the contact info."""
        self.pdf.set_draw_color(0, 0, 0)
        y_line = self.pdf.get_y() - 0.1   # Position line slightly above the current cursor
        self.pdf.line(self.profile_x, y_line, 20, y_line)

        # Move cursor down slightly to create space after the line
        self.pdf.set_xy(self.profile_x, self.pdf.get_y())

    def _add_description(self):
        """Add the multi‑line professional description."""
        desc_info = {
            "font": "Arial",
            "style": "",
            "size": 10,
            "width": 0,
            "height": 0.45,
            "ln": True,
            "desc": (
                "Fullstack Developer & Data Engineer, specialise en developpement d'applications web "
                "et en gestion de donnees. Competent en front-end/back-end et en ingenierie des donnees, "
                "je transforme les besoins metiers en solutions performantes. Rigoureux et motive, "
                "je suis ouvert a de nouvelles opportunites."
            )
        }
        self.pdf.set_font(desc_info["font"], desc_info["style"], desc_info["size"])
        self.pdf.multi_cell(desc_info["width"], desc_info["height"], desc_info["desc"])

        # After description, we can set the position for the next section title
        self.pdf.set_xy(self.default_x, self.default_y)

    def _add_skills_section(self):
        """Add a 'Skills' section with a title and placeholder content."""
        self._add_sections_title("Compétences Techniques")
        self._add_skills_section_subtitle("Développement Fullstack")
        skills_content = (
            "Front-End : HTML, CSS, JavaScript, React.js, Bootstrap, JQuery, Responsive/Mobile-first design, Optimisation web\n"
            "Back-End : PHP, Python, Laravel, Node.js, Express.js\n"
            "Mobile : React Native, Flutter\n"
            "Bases de données : MySQL, MongoDB\n"
            "DevOps & Outils : Git, GitHub, GitLab, Nginx, Linux, Shell scripting\n"
            "Méthodologies : Agile (Scrum)\n"
            "Sécurité : Sécurité des applications web, déploiement & maintenance serveurs"
        )
        self._format_text_to_list(skills_content)
        self._space_between_skills_sections()
        self._add_skills_section_subtitle("Ingénierie des Données")
        data_skills_content = (
            "Data Mining & Statistical Analysis\n"
            "Database Management: SQL & NoSQL (MySQL, MongoDB)\n"
            "Data Warehousing & Visualization: Power BI, Python (Pandas, Matplotlib, Seaborn)\n"
            "Big Data Fundamentals: data acquisition, processing & quality management\n"
            "Data Governance: data quality assurance & security"
        )
        self._format_text_to_list(data_skills_content)

    def _add_experience_section(self):
        """Add an 'Experience' section with a title and placeholder content."""
        self._add_sections_title("Expérience Professionnelle")
        experience_content = [
            {
                "company": "GivenX",
                "duration": "11/2025 - 03/2026",
                "title": "Développeur & Tech Lead",
                "tasks": (
                    "Conception, développement et déploiement d'applications web et mobiles.\n"
                    "Pilotage technique des projets : encadrement de l'équipe, répartition des tâches, revue de code et garantie de la qualité des livrables."
                )
            },
            {
                "company": "ClickDigital",
                "duration": "10/2025 - 02/2026",
                "title": "Développeur Web & Mobile",
                "tasks": (
                    "Développement de Flousafe (React.js, Next.js, Flutter) avec déploiement, sécurité et  optimisation des performances.\n"
                    "Conception d'interfaces responsives et modernes axées sur l'expérience utilisateur."
                )
            },
            {
                "company": "23Digit",
                "duration": "01/2025 - 06/2025",
                "title": "Développeur Full Stack (Stage)",
                "tasks": (
                    "Développement de solutions web et mobiles de gestion de caisse (Laravel, Node.js, React,React Native, Flutter).\n"
                    "Déploiement et maintenance des applications sur serveurs pour l'ensemble des projets livrés."
                )
            },
            {
                "company": "LMS Organisation & RH",
                "duration": "08/2024 - 10/2024",
                "title": "Développeur Intégration Systèmes (Stage)",
                "tasks": (
                    "Conception et intégration d'APIs et solutions middleware.\n"
                    "Documentation technique et optimisation des performances systèmes."
                )
            },
            {
                "company": "Groupe Scolaire Khawater",
                "duration": "05/2024",
                "title": "Développeur Systèmes Informatiques (Stage)",
                "tasks": (
                    "Migration vers une architecture microservices.\n"
                    "Gestion de l'infrastructure web et assistance technique."
                )
            }
        ]
        self._add_experience_content(experience_content)

    def _add_education_section(self):
        """Add an 'Education' section with a title and placeholder content."""
        self._add_sections_title("Formation")
        education_content = [
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
            }
        ]
        self._add_education_content(education_content)

    def _add_languages_section(self):
        """Add a 'Languages' section with a title and placeholder content."""
        self._left_align()
        self._add_sections_title("Langues")
        self._text_single_line(text="Arabe : Langue maternelle | Anglais : Intermédiaire | Français : Opérationnel")

    # ----------------------------------------------------------------------
    # Private methods to add section's component (e.g., title, subtitle, content)
    # ----------------------------------------------------------------------
    def _add_sections_title(self, title):
        """Add a section title (e.g., for skills or experience)."""
        self._text_single_line(variant="title", text=title, ln=True)

        self._left_align()

        # add a line under the section title
        self.pdf.set_draw_color(0, 0, 0)
        y_line = self.pdf.get_y()
        self.pdf.line(self.default_x, y_line, 20, y_line)

        self._space_after_line()

    def _add_skills_section_subtitle(self, subtitle):
        """Add a subtitle for the skills section (e.g., for a specific skill category)."""
        self._left_align()
        self._text_single_line(variant="subtitle", text=subtitle)
        self._space_after_subtitle()

    def _add_experience_content(self, experience_content):
        """Add the experience content with company, duration, title and tasks."""
        for exp in experience_content:
            self._left_align()
            # Company and duration
            self._text_single_line(variant="subtitle", text=f"{exp['company']}", ln=False)
            self._text_single_line(variant="subtitle", text=f"{exp['duration']}", align="R")

            self._space_between_experience_company_and_title()
            # Title
            self._left_align()
            self._text_single_line(text=exp["title"])

            self._space_after_experience_title()
            # Tasks (formatted as bullet points)
            self._format_text_to_list(exp["tasks"])
            self._space_between_experience_entries() if exp != experience_content[-1] else None  # Add space between entries except after the last one

    def _add_education_content(self, education_content):
        """Add the education content with formation and institution-duration."""
        for edu in education_content:
            # set position for each education entry
            self._left_align()
            # Formation
            self._text_single_line(text=f"{edu['formation']}", ln=False)
            self._text_single_line(text=f"{edu['institution-duration']}", ln=True, align="R")

            self._space_between_education_entries() if edu != education_content[-1] else None  # Add space between entries except after the last one

    # ----------------------------------------------------------------------
    # Private tools methods
    # ----------------------------------------------------------------------
    def _format_text_to_list(self, text):
        """Add skills content with safe bullet layout."""

        lines = text.split("\n")

        # safe usable width (A4 = 21cm, margins included)
        usable_width = 17.5  # adjust if needed

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Bullet
            self.pdf.set_xy(self.default_x + 0.2, self.pdf.get_y()) 
            self.pdf.set_font("DejaVu", "", 10)
            self.pdf.cell(0.4, 0.45, "•", ln=0, align="C")

            # Text (IMPORTANT: reset X properly)
            self.pdf.set_font("Arial", "", 10)
            self.pdf.set_xy(self.pdf.get_x(), self.pdf.get_y())

            self.pdf.multi_cell(usable_width, 0.45, line)

        self.pdf.set_xy(self.default_x, self.pdf.get_y())

    # ----------------------------------------------------------------------
    # Public method to save the generated PDF
    # ----------------------------------------------------------------------
    def save(self, filename="cv.pdf"):
        """Output the PDF to the given file."""
        self.pdf.output(filename)


# --------------------------------------------------------------------------
# Usage example (produces exactly the same output as the original script)
# --------------------------------------------------------------------------
if __name__ == "__main__":
    cv = CVGenerator()
    cv.save("Ouafik_Karam.pdf")