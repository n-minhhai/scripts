import os
import sys

def add_file_type_to_files(directory, filetype):
    """
    Add the specified file type to all files without a file type in the directory and its subdirectories.
    
    :param directory: The path to the directory.
    :param filetype: The file type to add (e.g., '.txt').
    """
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            if '.' not in filename:  # Check if the file has an extension
                original_path = os.path.join(foldername, filename)
                new_path = original_path + filetype
                os.rename(original_path, new_path)
                print(f"Renamed: {original_path} -> {new_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python add_filetype.py <directory_path> <filetype_to_add>")
        sys.exit(1)

    directory_path = sys.argv[1]
    filetype_to_add = sys.argv[2]

    add_file_type_to_files(directory_path, filetype_to_add)
