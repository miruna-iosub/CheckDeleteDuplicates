import os
import sys

def get_file_content(file_path):
    """
    Read and return the content of a file.

    Args:
        file_path (str): The path to the file.
    """
    with open(file_path, 'r') as file:
        return file.read()

def check_duplicates(directory_path):
    """
    Duplicate files in a directory based on their content.

    Args:
        directory_path (str): The path to the directory.
    """
    content_files = {}

    for root, _, files in os.walk(directory_path):
        for file in files:
            path_file = os.path.join(root, file)
            print(path_file)
            content = get_file_content(path_file)
            if content in content_files:
                content_files[content].append(path_file)
            else:
                content_files[content] = [path_file]

    return [files for files in content_files.values() if len(files) > 1]


def delete_duplicates(all_duplicate_files):
    """
    Delete duplicate files based on user input.

    Args:
        all_duplicate_files (list): A list of sets, where each set contains paths of files with identical content.
    """
    if not all_duplicate_files:
        print("There are no files with identical content found.")
    else:
        for index, files in enumerate(all_duplicate_files, start=1):
            print(f"Set {index}:")
            print("The following files have identical content:")
            for file_index, file_path in enumerate(files, start=1):
                print(f"   {file_index}. {file_path}")

            choice = input(f"Select the file you want to keep [1..{len(files)}] (or 'none' for none): ")

            if choice != 'none':
                try:
                    choice = int(choice)
                    if 1 <= choice <= len(files):
                        file_to_keep = files[choice - 1]
                        for file_path in files:
                            if file_path != file_to_keep:
                                if os.path.exists(file_path):
                                    os.remove(file_path)
                                    print(f"File deleted: {file_path}")
                                else:
                                    print(f"File not found: {file_path}")
                        print("Deletion complete.")
                    else:
                        print("Invalid choice.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                print("No files were deleted.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python remove_duplicates.py <directory_path>")
        print("Example: python remove_duplicates.py C:\\Users\\iosub\\OneDrive\\Documents\\GitHub\\PythonProjectC2023-2024\\test")
    else:
        directory_path = sys.argv[1]
        print(directory_path)
        all_duplicate_files = check_duplicates(directory_path)
        delete_duplicates(all_duplicate_files)

#python remove_duplicates.py C:\Users\iosub\OneDrive\Documents\GitHub\PythonProjectC2023-2024\test