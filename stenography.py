from PIL import Image
import numpy as np

def encode_message():
    image_path = input("Enter the path of the image to hide the message: ")
    message = input("Enter the secret message: ")
    output_path = input("Enter the output image path: ")

    img = Image.open(image_path)
    img_array = np.array(img, dtype=np.uint8)
    message += "@@@"
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    data_index = 0

    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            for k in range(img_array.shape[2]):
                if data_index < len(binary_message):
                    pixel_value = int(img_array[i][j][k]) 
                    pixel_value = (pixel_value & 254) | int(binary_message[data_index]) 
                    img_array[i][j][k] = np.uint8(pixel_value)  
                    data_index += 1
                else:
                    break

    encoded_img = Image.fromarray(img_array)
    encoded_img.save(output_path)
    print("Message encoded successfully!")

def decode_message():
    image_path = input("Enter the path of the image to extract the message: ")
    img = Image.open(image_path)
    img_array = np.array(img, dtype=np.uint8)
    binary_message = ""

    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            for k in range(img_array.shape[2]):
                binary_message += str(img_array[i][j][k] & 1)

    chars = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    message = ''.join(chr(int(char, 2)) for char in chars)
    print("Decoded Message:", message.split("@@@")[0])

while True:
    choice = input("Choose an option: \n1. Encode a message \n2. Decode a message \n3. Exit \nEnter choice: ")
    if choice == "1":
        encode_message()
    elif choice == "2":
        decode_message()
    elif choice == "3":
        break
    else:
        print("Invalid choice! Please try again.")
