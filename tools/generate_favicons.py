from PIL import Image
from pathlib import Path

root = Path(__file__).resolve().parents[1]
src = root / 'digi-calx-logo.png'
if not src.exists():
    raise SystemExit('Source logo not found: ' + str(src))

out_dir = root / 'assets' / 'png'
out_dir.mkdir(parents=True, exist_ok=True)

sizes = [16, 32, 48, 64, 96, 128, 180, 192, 256, 512]

logo = Image.open(src).convert('RGBA')
w, h = logo.size

for size in sizes:
    # create a transparent canvas
    canvas = Image.new('RGBA', (size, size), (255, 255, 255, 0))
    draw = Image.new('RGBA', (size, size), (255, 255, 255, 0))
    from PIL import ImageDraw

    # determine rounded rectangle parameters
    pad_ratio = 0.82
    inner_size = int(size * pad_ratio)
    # center the inner white rounded square
    inner_offset = ((size - inner_size) // 2, (size - inner_size) // 2)
    radius = max(1, int(size * 0.16))

    d = ImageDraw.Draw(draw)
    left = inner_offset[0]
    top = inner_offset[1]
    right = left + inner_size
    bottom = top + inner_size
    # draw white rounded rectangle onto the transparent draw layer
    d.rounded_rectangle([left, top, right, bottom], radius=radius, fill=(255, 255, 255, 255))

    # calculate logo scale to fit inside the rounded square with a bit of padding
    scale = min((inner_size * 0.92) / w, (inner_size * 0.92) / h)
    new_w = max(1, int(w * scale))
    new_h = max(1, int(h * scale))
    resized = logo.resize((new_w, new_h), Image.LANCZOS)
    offset = (left + (inner_size - new_w) // 2, top + (inner_size - new_h) // 2)

    # composite the white rounded background and then paste the logo using its alpha
    canvas = Image.alpha_composite(canvas, draw)
    canvas.paste(resized, offset, resized.split()[-1])

    out_path = out_dir / f'favicon-{size}.png'
    canvas.save(out_path, optimize=True)
    print('Wrote', out_path)

# Save the commonly used names
import shutil
# icon-192.png and icon-512.png for manifest
shutil.copyfile(out_dir / 'favicon-192.png', out_dir / 'icon-192.png')
shutil.copyfile(out_dir / 'favicon-512.png', out_dir / 'icon-512.png')
# apple touch icon (180)
shutil.copyfile(out_dir / 'favicon-180.png', out_dir / 'apple-touch-icon.png')

# Create favicon.ico in site root containing multiple sizes
ico_sizes = [(16,16),(32,32),(48,48),(64,64)]
base = Image.open(out_dir / 'favicon-512.png').convert('RGBA')
# create ICO from the RGBA image so transparency outside rounded corners is preserved
ico_path = root / 'favicon.ico'
base.save(ico_path, format='ICO', sizes=ico_sizes)
print('Wrote', ico_path)
