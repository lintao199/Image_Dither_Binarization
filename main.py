import argparse
import subprocess
import sys
from pathlib import Path

from PIL import Image


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Ordered dithering for images.")
    parser.add_argument("image", nargs="?", help="Path to input image.")
    parser.add_argument("-o", "--output", help="Path to save output image.")
    return parser.parse_args()


def select_image_path() -> str:
    if sys.platform == "darwin":
        try:
            result = subprocess.run(
                [
                    "osascript",
                    "-e",
                    'POSIX path of (choose file of type {"public.image"})',
                ],
                capture_output=True,
                text=True,
                check=True,
            )
            return result.stdout.strip()
        except Exception:
            pass
    image_file = input("Enter image path (drag and drop is OK): ").strip().strip('"')
    return image_file


def main() -> None:
    args = parse_args()
    image_file = args.image or select_image_path()
    if not image_file:
        print("No image selected. Exiting.")
        return

    image_path = Path(image_file).expanduser()
    if not image_path.exists():
        print(f"File not found: {image_path}")
        return

    img = Image.open(image_path).convert("RGB")
    img_width, img_height = img.size
    bayer = [
        [0, 48, 12, 60, 3, 51, 15, 63],
        [32, 16, 44, 28, 35, 19, 47, 31],
        [8, 56, 4, 52, 11, 59, 7, 55],
        [40, 24, 36, 20, 43, 27, 39, 23],
        [2, 50, 14, 62, 1, 49, 13, 61],
        [34, 18, 46, 30, 33, 17, 45, 29],
        [10, 58, 6, 54, 9, 57, 5, 53],
        [42, 26, 38, 22, 41, 25, 37, 21],
    ]

    out = Image.new("RGB", (img_width, img_height))
    in_pixels = img.load()
    out_pixels = out.load()

    for y in range(img_height):
        for x in range(img_width):
            r, g, b = in_pixels[x, y]
            gray = (r + g + b) // 12
            if gray < bayer[y & 7][x & 7]:
                out_pixels[x, y] = (0, 0, 0)
            else:
                out_pixels[x, y] = (255, 255, 255)

    if args.output:
        output_path = Path(args.output).expanduser()
    else:
        output_path = image_path.with_name(f"{image_path.stem}_dithered{image_path.suffix}")
    out.save(output_path)
    out.show()
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    main()


