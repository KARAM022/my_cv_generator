# CV Generator

This project generates a CV PDF from `main.py` using `fpdf`.

**What the script does**
- Builds a PDF CV with a profile image, name, contact line, summary, skills, experience, education, and languages.
- Saves the final file as `cv.pdf`.

## Requirements

- Python 3.7 or later
- `fpdf2` from `requirements.txt`
- `image.jpg` in the project root
- `DejaVuSans-Bold.ttf` in the project root

## Install

Create a virtual environment and install the dependency:

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If you are using Command Prompt or Git Bash, activate the virtual environment with the matching command for your shell.

## Usage

Run the script from the project root:

```bash
python main.py
```

The script creates `cv.pdf` in the same folder.

## Customization

- Edit `main.py` to change the name, contact details, summary, section text, or styling.
- Replace `image.jpg` if you want a different profile photo.
- Keep `DejaVuSans-Bold.ttf` available so the bullet points and Unicode text render correctly.

## Contact

Email: ouafik0karam@gmail.com

Phone: +212 608310554

LinkedIn: https://www.linkedin.com/in/karam-ouafik-67b040279

