import os, cv2, sys
from PIL import Image

GSCALE = "@#+~-` "   # 7 Levels of depth, 37 per character
PATH = 'frame.jpg'

def main():
    video = cv2.VideoCapture(0)
    video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    while True:
        ret, frame = video.read()
        frame = cv2.flip(frame, 1)
        cv2.imwrite(PATH, frame)
        print(ConvertToASCII())
        if sys.platform == 'win32':
            os.system('cls')
        else:
            os.system('clear')


def ConvertToASCII():
    # Resize and Convert to greyscale image
    img = Image.open(PATH)
    img = img.resize((100, 40))
    img = img.convert('L')

    # Get image data according greyscale
    pixels = img.getdata()
    new_pixels = [GSCALE[pixel // 37] for pixel in pixels]
    new_pixels = "".join(new_pixels)

    # Assign characters to the new pixel values
    new_pixels_count = len(new_pixels)
    ascii_image = [
        new_pixels[index: index + 100]
        for index in range(0, new_pixels_count, 100)
    ]
    ascii_image = "\n".join(ascii_image)

    # Return the ascii image
    return ascii_image

main()