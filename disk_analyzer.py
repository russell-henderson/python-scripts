import os
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt


def analyze_directory(directory):
    file_counts = {}
    all_files = []

    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            extension = os.path.splitext(file)[1] or 'No Extension'

            # Count file types
            if extension in file_counts:
                file_counts[extension] += 1
            else:
                file_counts[extension] = 1

            # Append file info to the list
            all_files.append((file_path, file_size))

    return file_counts, all_files


def export_to_txt(file_counts, largest_files, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:  # Specify UTF-8 encoding
        f.write("File Type Counts:\n")
        for ext, count in file_counts.items():
            f.write(f"{ext}: {count}\n")

        f.write("\nTop 100 Largest Files:\n")
        for file_info in largest_files:
            f.write(f"{file_info[0]}: {file_info[1]} bytes\n")


def plot_file_counts(file_counts):
    extensions = list(file_counts.keys())
    counts = list(file_counts.values())

    plt.figure(figsize=(10, 6))
    plt.barh(extensions, counts, color='skyblue')
    plt.xlabel('Number of Files')
    plt.ylabel('File Type')
    plt.title('File Count by Type')
    plt.tight_layout()
    plt.savefig('file_counts.png')
    plt.show()


def main():
    directory = input("Enter the directory path to analyze: ")
    file_counts, all_files = analyze_directory(directory)

    # Get the top 100 largest files
    largest_files = sorted(all_files, key=lambda x: x[1], reverse=True)[:100]

    # Print the results in a table format
    print("\nFile Type Counts:")
    print(tabulate(file_counts.items(), headers=[
          'File Type', 'Count'], tablefmt='pretty'))

    print("\nTop 100 Largest Files:")
    print(tabulate(largest_files, headers=[
          'File Location', 'Size (bytes)'], tablefmt='pretty'))

    # Export to text file
    export_to_txt(file_counts, largest_files, 'file_analysis.txt')
    print("\nAnalysis exported to file_analysis.txt")

    # Plot the file counts
    plot_file_counts(file_counts)


if __name__ == "__main__":
    main()
