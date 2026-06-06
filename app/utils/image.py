"""
Image preparation for the CV.

Scans assets/images/ for images.
If 'avatar.png' already exists, it means nothing to do.
Otherwise, picks the first available image (if multiple, the first alphabetically;
if exactly one, that one) and creates a round version saved as 'avatar.png'.
"""

from pathlib import Path
from PIL import Image, ImageDraw

from ..config import BASE_DIR

IMAGES_DIR = BASE_DIR / "assets" / "images"
AVATAR_NAME = "avatar.png"
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff"}


def _make_round_image(input_path: Path, output_path: Path) -> None:
    """Create a circular PNG from the input image and save it."""
    img = Image.open(input_path).convert("RGBA")

    size = min(img.size)
    img = img.resize((size, size))

    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)

    result = Image.new("RGBA", (size, size), (255, 255, 255, 0))
    result.paste(img, (0, 0), mask)

    result.save(output_path)


def prepare_avatar() -> None:
    """
    Ensure a round avatar image exists.

    If 'avatar.png' already exists, do nothing.
    Otherwise, scan the images directory for other images,
    pick the first one (sorted alphabetically) and create the round avatar.
    """
    avatar_path = IMAGES_DIR / AVATAR_NAME
    if avatar_path.exists():
        return  # nothing to do

    # Collect all image files except the avatar itself (shouldn't exist yet)
    image_files = sorted(
        p for p in IMAGES_DIR.glob("*")
        if p.suffix.lower() in IMAGE_EXTENSIONS
    )

    if not image_files:
        raise FileNotFoundError(
            f"No image files found in {IMAGES_DIR}. "
            "Please add at least one image to generate the CV profile picture."
        )

    # Use the first image found
    source = image_files[0]
    _make_round_image(source, avatar_path)