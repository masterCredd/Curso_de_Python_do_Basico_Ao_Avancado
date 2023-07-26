from pathlib import Path
from PIL import Image


ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER/'img_edit'/'_new.jpeg'
NEW_IMAGE = ROOT_FOLDER/'img_edit'/'new_DOG.jpeg'

pil_image = Image.open(ORIGINAL)
width, height = pil_image.size
exif = pil_image.info['exif']

# width     new_width
# height    ??
new_width = 640
new_heigth = round(height * new_width / width)

new_image = pil_image.resize(size=(new_width, new_heigth))
new_image.save(
    NEW_IMAGE,
    optimize=True,
    quality=70,
    # exif=exif,
)