# CV Generator

A modular, data‑driven PDF CV generator for a clean A4 résumé.  
Built with Python, `fpdf2` and Pillow – fully customisable from a single JSON file.

## Features

- **Data‑driven** – All content lives in `data/cv_data.json`.  
- **Auto‑round avatar** – Drop a photo in `assets/images/`; the script creates a perfectly circular `avatar.png` automatically.  
- **Unicode & bullet points** – Uses DejaVu Sans for special characters.  
- **Clean architecture** – Configuration, PDF helpers, and CV sections are separated for easy maintenance.  
- **One‑command generation** – Run `python run.py` and your PDF is ready.

## Repository structure

```
project_root/
│
├── data/
│   ├── cv_data.json.example     # Copy to cv_data.json and edit
│   └── cv_data.json             # (ignored – your personal data)
│
├── assets/
│   ├── fonts/
│   │   └── DejaVuSans-Bold.ttf
│   └── images/
│       ├── (your_photo).jpg     # Any image here will be used
│       └── avatar.png           # Generated automatically
│
├── app/
│   ├── __init__.py
│   ├── config.py                # Paths & layout constants
│   ├── main.py                  # CVGenerator class (orchestrator)
│   ├── sections/                # One module per CV block
│   │   ├── __init__.py
│   │   ├── profile.py           # Image, name, contact, description
│   │   ├── skills.py
│   │   ├── experience.py
│   │   ├── education.py
│   │   └── languages.py
│   └── utils/                   # Shared utilities
│       ├── __init__.py
│       ├── layout.py            # Position helpers (reset_x, add_space, draw_line)
│       ├── text.py              # Text rendering, bullets, section titles
│       └── image.py             # Image scanning & round avatar creation
│
├── run.py                       # Entry point
├── requirements.txt
├── .gitignore
└── output/                      # Generated PDFs (auto‑created, git‑ignored)
```

## Requirements

- Python ≥ 3.7
- Packages: `fpdf2`, `Pillow`  
  (install with `pip install -r requirements.txt`)

## Installation

1. **Clone the repository** and move into its folder.
2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv .venv
   ```
3. **Activate it**:
   - Windows PowerShell: `.venv\Scripts\Activate.ps1`
   - Windows CMD: `.venv\Scripts\activate.bat`
   - macOS / Linux: `source .venv/bin/activate`
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Prepare your data file**:
   ```bash
   cp data/cv_data.json.example data/cv_data.json
   ```
   Then edit `data/cv_data.json` with your own information.

## Usage

1. **Place a profile photo** inside `assets/images/`. It can be any common format (`.jpg`, `.png`, `.webp`, etc.).
2. **Run the generator**:
   ```bash
   python run.py
   ```
3. Your PDF will appear in the `output/` folder with the filename you set in `cv_data.json` (default: `Ouafik_Karam.pdf`).

## Customisation

- **Content** → edit `data/cv_data.json` – all sections can be added, removed, or reordered.
- **Layout & spacing** → modify the `Layout` class in `app/config.py`.
- **Fonts** → add new `.ttf` files to `assets/fonts/` and update `app/config.py` and `app/utils/text.py` accordingly.
- **Section order** → change the sequence of calls inside `app/main.py` (`CVGenerator.__init__`).

### Adding a new section

1. Create a new file in `app/sections/` (e.g. `hobbies.py`).
2. Write a function that receives `(pdf, data)` and uses helpers from `app/utils/`.
3. Import it in `app/main.py` and call it where needed.
4. Add the corresponding data to `data/cv_data.json`.

## Contributing

Contributions are welcome and appreciated!  
Whether you want to fix a bug, add a new feature, or propose a design improvement, here’s how you can help:

1. **Fork** the repository and create a new branch for your changes.
2. **Make your changes** – keep them focused and well documented.
3. **Test** that the PDF still generates correctly (`python run.py`).
4. **Submit a pull request** with a clear description of what you changed and why.

If you have ideas for bigger features (like themes or a UI), please open an issue first to discuss your approach.  
All contributions are reviewed with respect and constructive feedback.

## Roadmap / Future features

Planned improvements for the project:

- **Themes** – Switch between different visual styles (colour schemes, font pairings, section layouts) without touching code.
- **Web & mobile interface** – A browser‑based UI to edit CV data visually and preview the PDF in real time.
- **Multi‑language support** – Generate CVs in English, French, Arabic, or other languages from the same data.
- **Multiple page layouts** – Choose between classic, modern, or creative designs.
- **Export formats** – Option to generate DOCX or HTML alongside PDF.

Have an idea? Feel free to open an issue or contribute directly!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

**Karam Ouaifik**  
📧 ouafik0karam@gmail.com  
📞 +212 608310554  
🔗 [LinkedIn](https://www.linkedin.com/in/karam-ouafik-67b040279)