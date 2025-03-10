import os
import matplotlib.pyplot as plt
from collections import defaultdict

def analyze_directory(directory):
    """Analyze the given directory and return a count of file types."""
    file_types = defaultdict(int)

    for root, _, files in os.walk(directory):
        for file in files:
            # Get the file extension
            _, ext = os.path.splitext(file)
            # Increment the count for the file type
            file_types[ext] += 1

    return file_types

def save_results_to_txt(file_types, output_file):
    """Save the file type counts to a text file."""
    with open(output_file, 'w') as f:
        f.write("File Type Breakdown:\n")
        for ext, count in file_types.items():
            f.write(f"{ext or 'No Extension'}: {count}\n")

def plot_file_types(file_types):
    """Generate a bar graph of file type breakdowns."""
    # Prepare data for plotting
    file_types_sorted = dict(sorted(file_types.items(), key=lambda item: item[1], reverse=True))
    extensions = list(file_types_sorted.keys())
    counts = list(file_types_sorted.values())

    # Create the bar graph
    plt.figure(figsize=(10, 6))
    plt.bar(extensions, counts, color='blue')
    plt.xlabel('File Types')
    plt.ylabel('Number of Files')
    plt.title('File Type Breakdown')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Show the plot
    plt.show()

def main(directory):
    output_file = 'file_type_breakdown.txt'
    file_types = analyze_directory(directory)
    save_results_to_txt(file_types, output_file)
    plot_file_types(file_types)
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    # Replace 'your_directory' with the path of the directory you want to analyze
    your_directory = 'D:\Sound\Sound Effects'
    main(your_directory)
