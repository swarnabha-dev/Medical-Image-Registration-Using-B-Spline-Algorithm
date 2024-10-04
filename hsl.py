from PIL import Image, ImageEnhance
import colorsys

def change_hsl(image, hue_change, saturation_change, lightness_change):
    # Convert image to RGB if not already
    image = image.convert('RGB')
    
    # Load pixels
    pixels = image.load()

    for i in range(image.width):
        for j in range(image.height):
            # Get RGB values
            r, g, b = pixels[i, j]

            # Convert RGB to HSL
            h, l, s = colorsys.rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)

            # Modify HSL values
            h = (h + hue_change / 360.0) % 1.0  # Ensure hue wraps around
            s = max(0, min(1, s + saturation_change / 100.0))  # Clamp saturation
            l = max(0, min(1, l + lightness_change / 100.0))  # Clamp lightness

            # Convert back to RGB
            r, g, b = colorsys.hls_to_rgb(h, l, s)

            # Set new RGB values
            pixels[i, j] = (int(r * 255), int(g * 255), int(b * 255))

    return image

print(list(range(2, 11)))
for i in range(2, 11):
    image = Image.open(f'{i}_fixed.tiff')

    # Change HSL values: hue +140, saturation -15, lightness +24
    modified_image = change_hsl(image, hue_change=140, saturation_change=-15, lightness_change=24)

    # Save the modified image
    modified_image.save(f'{i}_color.tiff')
    print(str(i), "done")
