from PIL import Image


for i in range(2, 11):
    image = Image.open(f'{i}_reg.tiff')

    # Convert the image to RGB if it's not already in that mode
    image = image.convert('RGB')

    # Split the image into its Red, Green, and Blue channels
    r, g, b = image.split()

    # Invert the Blue channel
    b_inverted = Image.eval(b, lambda x: 255 - x)

    # Merge the channels back together, replacing the blue channel with the inverted one
    inverted_image = Image.merge('RGB', (r, g, b_inverted))

    # Save the modified image to a new TIFF file
    inverted_image.save(f'{i}_fixed.tiff')
    print(str(i) + " done")
