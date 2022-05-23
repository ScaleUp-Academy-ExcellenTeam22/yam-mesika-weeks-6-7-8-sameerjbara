from PIL import Image


def decrypt_message(file_path: str) -> str:
    """Returns the decrypted message from encrypted image
    by converting the location of each black pixel to a letter.
            Args:
                file_path (str): the path of the image.
            Returns:
                std: The decrypted message.
            Raises:
                none
            """
    image = Image.open(file_path)
    image_pixels = image.load()
    rows_size, cols_size = image.size
    decrypted_message = [chr(col) for row in range(0, rows_size) for col in range(0, cols_size)
                         if image_pixels[row, col] == 1]  # in order to check if the pixel color is black
    return str("".join(decrypted_message))


path = r"C:\Users\DELL\Desktop\pythonBook\week06\resources\code.png"
print(decrypt_message(path))
