# CV Generator

A small Python script that generates a PDF curriculum vitae using the `fpdf2` library.

**Quick summary:** run the script to produce `full_cv.pdf` from the repository root.

**Features**
- Generate a styled PDF CV with profile, skills, experience, education, and languages.
- Easy to customize by editing `main.py`.

## Requirements

- Python 3.7 or later
- `fpdf2` (listed in `requirements.txt`)

Install dependencies (recommended: use a virtual environment):

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Usage

Run the script to generate the CV PDF:

```bash
python main.py
```

The script saves `full_cv.pdf` in the repository root and prints a confirmation message.

## Customization

- Edit `main.py` to change the name, contact details, sections, or formatting.
- The script uses a small `PDF` class (subclass of `FPDF`) — you can add methods or tweak fonts/sizes as needed.

## Files

- `main.py` — main script that builds and saves the CV PDF.
- `requirements.txt` — Python dependency list (fpdf2).
- `README.md` — this file.

## Contributing

Feel free to open issues or submit PRs with improvements. For small edits, editing `main.py` and updating the README is sufficient.

## Contact

For questions or help, contact the repository owner:

- **Email:** ouafik0karam@gmail.com
- **Phone:** +212 608310554
- **LinkedIn:** https://www.linkedin.com/in/karam-ouafik-67b040279

