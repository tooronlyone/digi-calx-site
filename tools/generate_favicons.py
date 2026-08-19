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
    # create a solid white square background and center the logo inside it
    canvas = Image.new('RGBA', (size, size), (255, 255, 255, 255))
    # leave a small padding to avoid touching edges
    pad_ratio = 0.82
    scale = min((size * pad_ratio) / w, (size * pad_ratio) / h)
    new_w = max(1, int(w * scale))
    new_h = max(1, int(h * scale))
    resized = logo.resize((new_w, new_h), Image.LANCZOS)
    offset = ((size - new_w) // 2, (size - new_h) // 2)
    # paste using the alpha channel as mask to preserve logo shape on white
    canvas.paste(resized, offset, resized.split()[-1])
    # convert to RGB to flatten any alpha onto white background
    final = canvas.convert('RGB')
    out_path = out_dir / f'favicon-{size}.png'
    final.save(out_path, optimize=True)
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
# ensure ICO is created from an image with white background
base_rgb = base.convert('RGB')
ico_path = root / 'favicon.ico'
base_rgb.save(ico_path, format='ICO', sizes=ico_sizes)
print('Wrote', ico_path)
