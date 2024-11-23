import io
import contextlib
from PIL import Image

if __name__ == "__main__":
    with open("0.jpg", "rb") as f, open("test.webp", "wb") as outfile:
        img = Image.open(f).convert("RGB")
        output = io.BytesIO()
        converted = img.save(output, format="webp", quality=70)
        outfile.write(output.getbuffer())
