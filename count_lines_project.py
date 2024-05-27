import os
import argparse

def count_lines_in_file(file_path):
    with open(file_path, 'r', errors='ignore') as file:
        return sum(1 for _ in file)

def count_lines_in_directory(directory):
    total_lines = 0
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                total_lines += count_lines_in_file(file_path)
    return total_lines

def main():
    parser = argparse.ArgumentParser(description='Count lines of code in a project directory.')
    parser.add_argument('directory', type=str, help='The directory of the project.')
    
    args = parser.parse_args()
    directory = args.directory
    
    if not os.path.isdir(directory):
        print(f'Error: {directory} is not a valid directory.')
        return
    
    total_lines = count_lines_in_directory(directory)
    print(f'Total lines of code: {total_lines}')

if __name__ == '__main__':
    main()

