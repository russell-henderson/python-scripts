# Python Script Library

## Directory Analysis Tool

![Project Image](https://i.ibb.co/PzzL92Yx/dir-base.jpg) <!-- Replace with your image path -->

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](LICENSE)
[![Issues](https://img.shields.io/github/issues/username/repo.svg)](issues)
[![Stars](https://img.shields.io/github/stars/username/repo.svg)](stargazers)

## Description

The **Directory Analysis Tool** is a Python script that analyzes a specified directory to provide insights into file types and sizes. It generates a summary of the number of files by type, lists the top 100 largest files, and creates a visual representation of file counts by type.

## Features

- Count the number of files in a directory broken down by file type.
- List the top 100 largest files with their sizes and paths.
- Export the results to a text file.
- Generate a bar graph displaying file counts by type.

## Requirements

- Python 3.8 or higher
- `matplotlib` for graph generation
- `tabulate` for formatted output

### Installation

You can install the required packages using pip:

```bash
pip install matplotlib tabulate
```

## Usage

1. Clone the repository to your local machine:

```bash
git clone https://github.com/username/repo.git
```

2. Navigate to the project directory:

```bash
cd repo
```

3. Run the script:

```bash
python directory_analysis.py
```

4. Enter the path to the directory you want to analyze when prompted.

## Example Output

- A text file named `file_analysis.txt` containing:
  - File type counts
  - A list of the top 100 largest files

- A bar graph saved as `file_counts.png`, showing the number of files by type.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Matplotlib](https://matplotlib.org/) for graphing capabilities.
- [Tabulate](https://pypi.org/project/tabulate/) for formatted table output.
