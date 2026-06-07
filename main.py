from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 16)
        self.cell(0, 10, "Ouafik Karam", new_x="LMARGIN", new_y="NEXT", align="C")
        self.ln(2)

        self.set_font("Helvetica", "", 11)
        self.cell(0, 8, "Casablanca | +212 608-310554 | ouafik0karam@gmail.com", new_x="LMARGIN", new_y="NEXT", align="C")
        self.ln(5)

    def section_title(self, title):
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(0, 0, 0)
        self.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def section_text(self, text):
        self.set_font("Helvetica", "", 11)
        self.multi_cell(0, 6, text)
        self.ln(2)


pdf = PDF()
pdf.add_page()

# ---------------- PROFILE ----------------
pdf.section_title("Profil")
pdf.section_text(
    "Fullstack Developer & Data Engineer specialise en developpement d'applications web et en gestion de donnees. "
    "Competent en front-end/back-end et en ingenierie des donnees, je transforme les besoins metiers en solutions performantes. "
    "Rigoureux et motive, ouvert a de nouvelles opportunites."
)

# ---------------- COMPETENCES ----------------
pdf.section_title("Competences Techniques")

pdf.section_text(
    "Data Engineering:\n"
    "- Data Mining & Statistical Analysis\n"
    "- SQL & NoSQL (MySQL, MongoDB)\n"
    "- Data Warehousing, Power BI, Python (Pandas, Matplotlib)\n"
    "- Big Data & Data Quality\n\n"
    "Fullstack:\n"
    "- HTML, CSS, JavaScript, React.js, Bootstrap\n"
    "- PHP, Python, Laravel, Node.js, Express.js\n"
    "- React Native, Flutter\n"
    "- Git, GitHub, Linux, Agile Scrum"
)

# ---------------- EXPERIENCE ----------------
pdf.section_title("Experiences Professionnelles")

pdf.section_text(
    "GivenX (11/2025 - 03/2026)\n"
    "Tech Lead & Developpeur\n"
    "- Pilotage technique et encadrement d'equipe\n"
    "- Developpement web & mobile\n\n"

    "ClickDigital (10/2025 - 02/2026)\n"
    "Developpeur Web & Mobile\n"
    "- Developpement d'applications web/mobile\n"
    "- UI/UX responsive\n\n"

    "23Digit (01/2025 - 06/2025)\n"
    "Developpeur Full Stack (Stage)\n"
    "- Front-end & back-end development\n"
    "- Deploiement & maintenance\n\n"

    "LMS Organisation & RH (08/2024 - 10/2024)\n"
    "- APIs & middleware\n"
    "- Optimisation des systemes\n\n"

    "Groupe Scolaire Khawater (05/2024)\n"
    "- Migration microservices\n"
    "- Infrastructure web"
)

# ---------------- FORMATION ----------------
pdf.section_title("Formation")

pdf.section_text(
    "- ENSAM : Licence en Ingenierie des Donnees (2025)\n"
    "- ALX : Certificat Genie Logiciel (2024)\n"
    "- OFPPT : Developpement Digital Web Full Stack (2024)\n"
    "- Bac SVT (2022)"
)

# ---------------- LANGUES ----------------
pdf.section_title("Langues")

pdf.section_text(
    "- Arabe : Langue maternelle\n"
    "- Anglais : Intermediaire\n"
    "- Francais : Operationnel"
)

# ---------------- SAVE ----------------
pdf.output("full_cv.pdf")

print("PDF created successfully: full_cv.pdf")