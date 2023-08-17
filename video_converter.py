import os
import subprocess
import argparse

# Run command example: python video_converter.py "C:\Videos" .MOV .MP4

def convert_files(path, file_extension, output_extension):
    for filename in os.listdir(path):
        if filename.endswith(file_extension):
            full_file_path = os.path.join(path, filename)
            output_file_path = os.path.join(path, filename.replace(file_extension, output_extension))
            subprocess.run(['ffmpeg', '-i', full_file_path, output_file_path])

    print(f"Conversion from {file_extension} to {output_extension} completed!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert media files using ffmpeg.')
    parser.add_argument('path', type=str, help='Path to directory containing files to convert.')
    parser.add_argument('input_ext', type=str, help='Input file extension (e.g. .MOV).')
    parser.add_argument('output_ext', type=str, help='Output file extension (e.g. .MP4).')
    
    args = parser.parse_args()
    
    convert_files(args.path, args.input_ext, args.output_ext)
