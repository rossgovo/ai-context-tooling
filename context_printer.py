import os
import sys
import argparse

def read_file(file_path, max_size=1 * 1024 * 1024):
    try:
        if os.path.getsize(file_path) <= max_size:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        else:
            return f"File too large to read (>{max_size} bytes)"
    except Exception as e:
        return f"Error reading file: {e}"

def list_files(directory, recursive=False):
    file_list = []
    if recursive:
        for root, _, files in os.walk(directory):
            for file in files:
                file_list.append(os.path.join(root, file))
    else:
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                file_list.append(file_path)
    return file_list

def main():
    parser = argparse.ArgumentParser(description="Process some files or directories.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--directory', type=str, help='Directory path')
    group.add_argument('--files', type=str, nargs='+', help='List of file paths')
    parser.add_argument('--recursive', action='store_true', help='Recursively include files from subdirectories')

    args = parser.parse_args()

    files_to_process = []

    if args.directory:
        files_to_process = list_files(args.directory, args.recursive)
    elif args.files:
        files_to_process = args.files

    print("Below are the files for the context of the query, files are separated by ====")
    print("====")
    for file_path in files_to_process:
        relative_path = os.path.relpath(file_path)
        contents = read_file(file_path)
        print(f"Filename: {relative_path}")
        print(f"Contents: {contents}")
        print("====")

if __name__ == "__main__":
    main()
