# Useful Python Scripts

![Project Image](https://i.ibb.co/PzzL92Yx/dir-base.jpg) <!-- Replace with your image path -->

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](LICENSE)
[![Issues](https://img.shields.io/github/issues/russell-henderson/repo.svg)](issues)
[![Stars](https://img.shields.io/github/stars/russell-henderson/repo.svg)](stargazers)

### Python Scripts with Descriptions

1. [Disk Analyzer](#disk-analyzer) - Analyzes disk usage and provides a summary of space consumed by files and directories.
2. [Directory Health Analyzer](#directory-health-analyzer) - Analyzes the health of a directory and provides a breakdown of file types.
3. [URL Extractor](#URL-Extractor-Script) - Scrapes data from websites and saves it in a structured format (e.g., CSV, JSON).

---
![Project Image](https://i.ibb.co/G4zRHT9D/base.jpg)
## Disk Analyzer

The **Directory Analysis Tool** is a Python script that analyzes a specified directory to provide insights into file types and sizes. It generates a summary of the number of files by type, lists the top 100 largest files, and creates a visual representation of file counts by type.

### Features

- Count the number of files in a directory broken down by file type.
- List the top 100 largest files with their sizes and paths.
- Export the results to a text file.
- Generate a bar graph displaying file counts by type.

### Requirements

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
git clone https://github.com/russell-henderson/python-scripts.git
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

### Example Output

- A text file named `file_analysis.txt` containing:
  - File type counts
  - A list of the top 100 largest files

- A bar graph saved as `file_counts.png`, showing the number of files by type.

#### Contributing

Contributions are welcome! Please open an issue or submit a pull request.

#### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

#### Acknowledgments

- [Matplotlib](https://matplotlib.org/) for graphing capabilities.
- [Tabulate](https://pypi.org/project/tabulate/) for formatted table output.

---

## Directory Health Analyzer

This Python script analyzes a specified directory, counts the occurrences of different file types, and generates a text file listing the results as well as a bar graph visualizing the breakdown of the files by type.

### Features

- Recursively traverses a specified directory to count file types.
- Saves the breakdown of file types to a text file.
- Generates a bar graph for visual representation of file type distribution.

### Prerequisites

- Python 3.x
- `matplotlib` library for plotting the graph

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/russell-henderson/python-scripts.git
   cd directory-health-analyzer
   ```

2. **Install required libraries:**
   You can install the required libraries using `pip`. Make sure you have `matplotlib` installed:

   ```bash
   pip install matplotlib
   ```

### Usage

1. **Modify the script:**
   Open the `analyze_directory.py` file and replace the `your_directory` variable in the `main` function with the path of the directory you want to analyze.

   ```python
   your_directory = 'path/to/your/directory'
   ```

2. **Run the script:**
   Execute the script using Python:

   ```bash
   python analyze_directory.py
   ```

3. **Output:**
   - The script will create a text file named `file_type_breakdown.txt` in the same directory as the script, which contains the count of each file type found.
   - A bar graph will be displayed showing the distribution of file types.

### Example Output

- The text file `file_type_breakdown.txt` will look like this:

```
  File Type Breakdown:
  .jpg: 10
  .png: 5
  .txt: 15
  No Extension: 3
  ```

- The bar graph will visually represent the counts of each file type.

#### Contributing

Contributions are welcome! If you find any issues or want to enhance the script, feel free to create a pull request.

#### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

#### Acknowledgments

- This script uses the `os` and `matplotlib` libraries for directory traversal and data visualization, respectively.

---

## URL Extractor Script

A simple Python script that extracts all URLs from a specified webpage and saves them to a CSV file. This script utilizes the `requests` library for HTTP requests and `BeautifulSoup` for parsing HTML.

### Features

- Fetches all hyperlinks (`<a>` tags) from a given webpage.
- Saves the extracted URLs to a CSV file.
- Handles HTTP errors gracefully.
- Avoids duplicate URLs by using a set data structure.

### Requirements

- Python 3.x
- `requests` library
- `BeautifulSoup4` library

### Installation

1. **Install Python**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Libraries**: Open your command line or terminal and run the following command:

   ```bash
   pip install requests beautifulsoup4
   ```

3. **Download the Script**: Save the script as `extract_urls.py`.

### Usage

1. Open your command line or terminal.
2. Navigate to the directory where you saved `extract_urls.py`.
3. Execute the script with the target URL and desired output CSV file name as arguments:

   ```bash
   python extract_urls.py <URL> <output.csv>
   ```

   - Replace `<URL>` with the website you want to analyze (e.g., `https://example.com`).
   - Replace `<output.csv>` with the desired name for the output file (e.g., `urls.csv`).

### How It Works

1. The script takes a URL as input and makes an HTTP GET request to fetch the webpage content.
2. It checks for any HTTP errors and handles exceptions accordingly.
3. Using BeautifulSoup, it parses the HTML content and finds all `<a>` tags with `href` attributes.
4. The URLs are collected in a set to ensure there are no duplicates.
5. Finally, the script writes the unique URLs to a specified CSV file.

### Example

To extract URLs from `https://example.com` and save them to a file named `output.csv`, run the following command:

```bash
python extract_urls.py https://example.com output.csv
```

After execution, you will find a file named `output.csv` in the same directory containing all the extracted URLs.

#### Notes

- Ensure you comply with the website's `robots.txt` and terms of service before scraping.
- The script currently only collects absolute URLs that start with `http` or `https`. You may modify the script to include relative URLs by adjusting the URL handling logic.
- The script may not work correctly for websites that use JavaScript to render content dynamically, as it only fetches the static HTML.

#### License

This script is provided as-is without warranty of any kind. Feel free to modify and use it for personal or educational purposes. If you plan to use it in a commercial application, please ensure compliance with the relevant licenses and legal requirements.
