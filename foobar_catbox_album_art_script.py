import requests
import sys
import traceback
from PIL import Image, ImageDraw
import io

QUALITY = 70

try:
    sys.stdin.reconfigure(encoding="utf-8")
    filename = sys.stdin.read().strip()

    with open(filename, "rb") as f:
        compressed_image = Image.open(f).convert("RGB")
        output = io.BytesIO()
        compressed_image.save(output, format="webp", quality=QUALITY)
        data = {
            "reqtype": (None, "fileupload"),
            "time": (None, "1h"),
            "fileToUpload": output.getbuffer(),
        }
        r = requests.post(
            "https://litterbox.catbox.moe/resources/internals/api.php", files=data
        )

    if not r.ok:
        print(r.text[:1000])
        exit(1)

    print(r.text, end="")

except:
    traceback.print_exc(file=sys.stdout)
    exit(1)
