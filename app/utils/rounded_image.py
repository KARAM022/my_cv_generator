from pathlib import Path
from PIL import Image, ImageDraw

def make_round_image(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")

    size = min(img.size)
    img = img.resize((size, size))

    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)

    result = Image.new("RGBA", (size, size), (255, 255, 255, 0))
    result.paste(img, (0, 0), mask)

    result.save(output_path)

if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parents[2]
    input_image = base_dir / "assets" / "images" / "image.jpg"
    output_image = base_dir / "assets" / "images" / "image.png"

    make_round_image(input_image, output_image)