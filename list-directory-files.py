import os


def list_files(startpath):
    with open('file_structure.txt', 'w') as f:
        for root, dirs, files in os.walk(startpath):
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            f.write('{}{}/\n'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for file in files:
                f.write('{}{}\n'.format(subindent, file))


if __name__ == "__main__":
    # Change this to your desired directory
    directory = r"C:/Users/YourUsername/Documents"
    # Check if the directory exists
    if os.path.isdir(directory):
        list_files(directory)
        print("File structure has been written to 'file_structure.txt'.")
    else:
        print("The specified path is not a valid directory. Please check the path and try again.")
