import os
from PIL import Image

ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    (original_width, original_height) = image.size
    aspect_ratio = original_height / float(original_width)
    new_height = int(aspect_ratio * new_width)
    return image.resize((new_width, new_height))

def grayscale_image(image):
    return image.convert("L")

def map_pixels_to_ascii(image, ascii_chars=ASCII_CHARS):
    pixels = image.getdata()
    new_pixels = [ascii_chars[pixel // 32] for pixel in pixels]
    return ''.join(new_pixels)

def convert_image_to_ascii(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file {image_path}. {e}")
        return

    image = resize_image(image, new_width)
    image = grayscale_image(image)
    ascii_str = map_pixels_to_ascii(image)
    num_of_pixels = len(ascii_str)
    ascii_image = [ascii_str[index: index + new_width] for index in range(0, num_of_pixels, new_width)]
    return '\n'.join(ascii_image)

def save_ascii_art(ascii_art, output_path):
    with open(output_path, 'w') as f:
        f.write(ascii_art)

def convert_frames_to_ascii(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")
            ascii_art = convert_image_to_ascii(input_path)
            save_ascii_art(ascii_art, output_path)
            print(f"Converted {filename} to ASCII art.")

convert_frames_to_ascii('frames', 'ASCIIframes')

