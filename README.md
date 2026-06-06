# CV Generator

This project generates a CV PDF from `main.py` using `fpdf`.

**What the scripts do**
- `rounded_image.py` converts `image.jpg` into a rounded `image.png` used in the PDF header.
- `main.py` builds a PDF CV with a profile image, name, contact line, summary, skills, experience, education, and languages.
- The script saves the final file as `Ouafik_Karam.pdf` by default.

## Requirements

- Python 3.7 or later
- `fpdf2` from `requirements.txt`
-- `image.jpg` (source photo) in the project root
-- `rounded_image.py` (helper) in the project root — produces `image.png`
-- `image.png` (rounded profile image) in the project root — used by `main.py`
-- `DejaVuSans-Bold.ttf` in the project root

## Install

Create a virtual environment and install the dependency:

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If you are using Command Prompt or Git Bash, activate the virtual environment with the matching command for your shell.

## Usage

Create a rounded profile image and run the generator from the project root:

```bash
# create a rounded PNG from image.jpg
python rounded_image.py

# generate the PDF
python main.py
```

The script creates `Ouafik_Karam.pdf` in the same folder by default.

## Customization

- Edit `main.py` to change the name, contact details, summary, section text, or styling.
-- Replace `image.jpg` to use a different profile photo; run `rounded_image.py` afterwards to regenerate `image.png`.
-- Keep `DejaVuSans-Bold.ttf` available so the bullets and Unicode text render correctly.

## Contact

Email: ouafik0karam@gmail.com

Phone: +212 608310554

LinkedIn: https://www.linkedin.com/in/karam-ouafik-67b040279

