import os
import shutil

def categorize_files(source_path, destination_path):
    audio_extensions = ['.mp3', '.wav', '.ogg']
    video_extensions = ['.mp4', '.mkv', '.avi']
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']

    for root, dirs, files in os.walk(source_path):
        for file in files:
            file_path = os.path.join(root, file)
            _, extension = os.path.splitext(file)

            if extension.lower() in audio_extensions:
                copy_to_directory(file_path, destination_path, 'Audio')
            elif extension.lower() in video_extensions:
                copy_to_directory(file_path, destination_path, 'Video')
            elif extension.lower() in image_extensions:
                copy_to_directory(file_path, destination_path, 'Images')

def copy_to_directory(file_path, destination_path, category):
    category_directory = os.path.join(destination_path, category)

    if not os.path.exists(category_directory):
        os.makedirs(category_directory)

    shutil.copy(file_path, os.path.join(category_directory, os.path.basename(file_path)))

if __name__ == "__main__":
    source_path = "/path/to/source"  # Replace with the actual source path
    destination_path = "/path/to/destination"  # Replace with the actual destination path

    categorize_files(source_path, destination_path)
