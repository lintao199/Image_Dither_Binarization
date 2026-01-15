# Repository Guidelines

## Project Structure & Module Organization
- `README.md` explains the dithering concept and the Bayer matrix used.
- `图像抖动算法处理图片.py` is the single entry-point script that loads an image, applies ordered dithering, and displays the result.
- There are no separate modules, tests, or assets directories at the moment.

## Build, Test, and Development Commands
- Install dependencies (NumPy + Pillow):
  - `pip install numpy pillow`
- Run the script locally:
  - `python "图像抖动算法处理图片.py"`
  - Update `image_file` inside the script to point to your local input image.
- There is no build step or packaging workflow configured.

## Coding Style & Naming Conventions
- Python, 4-space indentation; keep line length reasonable (PEP 8 style).
- Prefer `snake_case` for variables and functions if you refactor into helpers.
- No formatter or linter is configured; keep edits minimal and consistent with the current script style.

## Testing Guidelines
- No automated tests are present.
- Manual verification: run the script with a sample image and visually confirm that the output dithering looks correct.
- If you add tests later, keep them under a `tests/` directory and name files `test_*.py`.

## Commit & Pull Request Guidelines
- Commit history uses short, direct messages like `Update README.md`.
  - Follow the same concise, imperative style for consistency.
- PRs should include:
  - A brief description of the change and its impact on output.
  - A sample input image and the resulting output (or a screenshot) when visual behavior changes.
  - Any assumptions about image format, size, or color depth.

## Configuration & Usage Notes
- `image_file` is a local path; keep it configurable if you expand the script.
- The Bayer matrix assumes 8x8 ordered dithering; adjust carefully if you experiment with different matrices.
