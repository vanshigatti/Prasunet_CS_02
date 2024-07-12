from PIL import Image
import os

def encrypt_image(image_path):
    try:
        image = Image.open(image_path)
        width, height = image.size
        pixels = image.load()
        for y in range(height):
            for x in range(width):
                if image.mode == "RGB":
                    r, g, b = pixels[x, y]
                    pixels[x, y] = (g, b, r)  
                elif image.mode == "L":
                    pixel_value = pixels[x, y]
                    pixels[x, y] = min(pixel_value + 10, 255)
                    
        encrypted_image_path = os.path.splitext(image_path)[0] + "_encrypted.png"
        image.save(encrypted_image_path)
        print("Image encrypted successfully!")
        return encrypted_image_path
    except Exception as e:
        print("Error encrypting image:", e)
        return None

def decrypt_image(encrypted_image_path):
    try:
        encrypted_image = Image.open(encrypted_image_path)
        width, height = encrypted_image.size
        pixels = encrypted_image.load()
        for y in range(height):
            for x in range(width):
                if encrypted_image.mode == "RGB":
                    r, g, b = pixels[x, y]
                    pixels[x, y] = (b, r, g)  
                elif encrypted_image.mode == "L":
                    pixel_value = pixels[x, y]
                    pixels[x, y] = max(pixel_value - 10, 0)

        decrypted_image_path = encrypted_image_path.split('_encrypted')[0] + "_decrypted.png"
        encrypted_image.save(decrypted_image_path)
        print("Image decrypted successfully!")
        return decrypted_image_path
    except Exception as e:
        print("Error decrypting image:", e)

original_image_path = "sky.png"
encrypted_image_path = encrypt_image(original_image_path)
if encrypted_image_path:
    decrypted_image_path = decrypt_image(encrypted_image_path)

import matplotlib.pyplot as plt
def display_image(image_path, title):
    img = Image.open(image_path)
    plt.imshow(img)
    plt.title(title)
    plt.axis('off')
    plt.show()

original_image_path = "sky.png"
display_image(original_image_path, "Original Image")

encrypted_image_path = encrypt_image(original_image_path)  
if encrypted_image_path:
    display_image(encrypted_image_path, "Encrypted Image")

decrypted_image_path = decrypt_image(encrypted_image_path)  
if decrypted_image_path:
    display_image(decrypted_image_path, "Decrypted Image")
