# CV Generator

This project generates a CV PDF from the reorganized code under `app/` and stores generated files in `output/`.

What the repository contains
- `app/main.py` — the class-based CV generator. It reads assets under `assets/` and writes PDFs to `output/`.
- `app/utils/rounded_image.py` — helper that converts `assets/images/image.jpg` → `assets/images/image.png` (rounded).
- `assets/images/` — image assets (`image.jpg`, `image.png`).
- `assets/fonts/` — font files (e.g. `DejaVuSans-Bold.ttf`).
- `output/` — generated PDFs (created automatically by `app/main.py`).
- `requirements.txt`, `README.md`, `.gitignore` at repository root.

Quick summary
- Run `app/utils/rounded_image.py` to prepare the rounded profile image.
- Run `app/main.py` to generate the CV PDF. The default output file is written to `output/Ouafik_Karam.pdf`.

## Requirements

- Python 3.7 or later
- Dependencies listed in `requirements.txt` (`fpdf2`, `Pillow`)

## Install

Create and activate a virtual environment, then install dependencies:

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1   # PowerShell
python -m pip install -r requirements.txt
```

If you use Command Prompt or Git Bash, use the corresponding venv activation command for your shell.

## Usage

1. Put your source photo at `assets/images/image.jpg` (replace the existing file if present).
2. Generate the rounded image (this writes `assets/images/image.png`):

```bash
python app/utils/rounded_image.py
```

3. Generate the PDF (creates `output/Ouafik_Karam.pdf` by default):

```bash
python app/main.py
```

Notes
- `app/main.py` resolves asset paths relative to the repository and expects fonts in `assets/fonts/` and images in `assets/images/`.
- The `output/` directory is created automatically; add `output/` to `.gitignore` if you don't want generated PDFs tracked.

## Customization

- Edit `app/main.py` to change displayed name, contact details, section text, or styling.
- Replace `assets/images/image.jpg` with a different photo and re-run `app/utils/rounded_image.py`.
- Add or replace font files in `assets/fonts/` as needed.

## Contact

Email: ouafik0karam@gmail.com

Phone: +212 608310554

LinkedIn: https://www.linkedin.com/in/karam-ouafik-67b040279

