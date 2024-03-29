import os
import pyvips
import time
from pathlib import Path

def crop_image_with_coordinates(input_file, output_file, x_cord, y_cord, width, height):
    # Load the image
    image = pyvips.Image.new_from_file(input_file)
    
    # Crop the image
    cropped_image = image.extract_area(x_cord, y_cord, width, height)
    
    # Save the cropped image
    cropped_image.write_to_file(output_file)

def crop_images_in_folder(input_folder, output_folder, x_cord, y_cord, width, height):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # start timer
    start_time = time.time()

    # Loop through all files and folders in the input folder
    for item in os.listdir(input_folder):
        item_path = os.path.join(input_folder, item)
        
        # If item is a directory, recursively call crop_images_in_folder
        if os.path.isdir(item_path):
            # Create corresponding subfolder in the output directory
            sub_output_folder = os.path.join(output_folder, item)
            crop_images_in_folder(item_path, sub_output_folder, x_cord, y_cord, width, height)
        # If item is a file and is an image, crop it
        elif item.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
            # Crop the image with selected coordinates
            output_file = os.path.join(output_folder, item)
            crop_image_with_coordinates(item_path, output_file, x_cord, y_cord, width, height)

    # End timing
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time taken: {total_time:.2f} seconds")

def main():
    # Specify input and output folders
    input_folder = Path("pearls")
    output_folder = Path("cropped")

    # Specify the coordinates for cropping
    x_cord = 1350   # x_cord coordinate of the cropping area
    y_cord = 1100    # y_cord coordinate of the cropping area
    width = 1200  # Width of the cropping area
    height = 900 # Height of the cropping area

    # Crop images in the input folder with selected coordinates
    crop_images_in_folder(input_folder, output_folder, x_cord, y_cord, width, height)

if __name__ == '__main__':
    main()
