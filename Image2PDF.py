import os
from PIL import Image
from PyPDF2 import PdfMerger
import io

def convert_images_to_pdf(image_folder, output_pdf):
    # Get list of image files in the folder
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    image_files.sort()  # Sort the files to maintain order

    # Create a PdfMerger object
    merger = PdfMerger()

    # Iterate through the images
    for image_file in image_files:
        img_path = os.path.join(image_folder, image_file)
        
        # Open the image using Pillow
        img = Image.open(img_path)
        
        # Convert the image to RGB mode if it's not already
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Create a byte stream for the PDF
        img_byte_arr = io.BytesIO()
        
        # Save the image as PDF to the byte stream
        img.save(img_byte_arr, format='PDF')
        
        # Move to the beginning of the byte stream
        img_byte_arr.seek(0)
        
        # Append the image (now a PDF) to the merger
        merger.append(img_byte_arr)

    # Write out the merged PDF
    merger.write(output_pdf)
    merger.close()

# Example usage
image_folder = r'C:\Users\siddh\Desktop\pdf\IL'
output_pdf = 'output.pdf'
convert_images_to_pdf(image_folder, output_pdf)