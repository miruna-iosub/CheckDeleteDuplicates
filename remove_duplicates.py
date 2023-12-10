import os

def get_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def check_duplicates(folder):
    content_files = {}

    for root, _, files in os.walk(folder):
        for file in files:
            path_file = os.path.join(root, file)
            content = get_file_content(path_file)
            if content in content_files:
                content_files[content].append(path_file)
            else:
                content_files[content] = [path_file]

    return [files for files in content_files.values() if len(files) > 1]

if __name__ == "__main__":
    folder = input("Enter the path to the folder: ")
    print(folder)
    all_duplicate_files = check_duplicates(folder)
