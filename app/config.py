from pathlib import Path


# Base paths
BASE_DIR = Path(__file__).resolve().parents[1]
FONT_PATH = BASE_DIR / "assets" / "fonts" / "DejaVuSans-Bold.ttf"
IMAGE_PATH = BASE_DIR / "assets" / "images" / "avatar.png"
OUTPUT_DIR = BASE_DIR / "output"
DATA_PATH = BASE_DIR / "data" / "cv_data.json"


class Layout:
    # Profile block
    PROFILE_X = 5.4
    PROFILE_Y = 0.1
    PROFILE_MARGIN_AFTER_NAME = 0.3

    # Section placement (after profile)
    SECTION_X = 1.25
    SECTION_Y_START = 4.0

    # Spacing constants
    SPACE_AFTER_LINE = 0.3
    SPACE_AFTER_SUBTITLE = 0.1
    SPACE_BETWEEN_SKILLS_SECTIONS = 0.1
    SPACE_BETWEEN_SECTIONS = 0.4
    SPACE_BETWEEN_EXPERIENCE_COMPANY_AND_TITLE = 0.1
    SPACE_AFTER_EXPERIENCE_TITLE = 0.1
    SPACE_BETWEEN_EXPERIENCE_ENTRIES = 0.3
    SPACE_BETWEEN_EDUCATION_ENTRIES = 0.1