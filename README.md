# Secure Data Hiding in Images Using Steganography

## Introduction
This project implements **LSB (Least Significant Bit) Steganography** to securely hide and extract secret messages within images. The tool ensures data privacy by making hidden information invisible to unauthorized users.

## Features
- **LSB-based image steganography** for secure data embedding
- **Efficient encoding and decoding** with minimal image distortion
- **Supports all image formats** (PNG, JPG, etc.)
- **Interactive user input** for easy operation
- **Maintains image quality** after hiding data

## Technologies Used
- **Python**
- **Pillow (PIL)** – Image processing
- **NumPy** – Array manipulation
- **OpenCV (Optional)** – Additional image handling

## Installation
To run this project, install the required dependencies using:
```sh
pip install pillow numpy opencv-python
```

## Usage
### Encoding a Message
Run the script and follow the prompts:
```sh
python stenography.py
```
Select option `1` to encode a message:
- Enter the **image path**
- Enter the **secret message**
- Enter the **output image path**

### Decoding a Message
Select option `2` to decode a message:
- Enter the **stego image path**
- The hidden message will be displayed

### Example
```sh
Enter the path of the image to hide the message: input.png
Enter the secret message: Hello, World!
Enter the output image path: output.png
Message encoded successfully!
```

## Future Enhancements
- Support for **audio and video steganography**
- Additional **encryption layers** for more security
- Web and mobile application integration


## Author
**Himanshu Yadav**

