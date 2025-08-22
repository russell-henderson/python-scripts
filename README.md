# Useful Python Scripts

![Project Image](https://i.ibb.co/PzzL92Yx/dir-base.jpg) <!-- Replace with your image path -->

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](LICENSE)
[![Issues](https://img.shields.io/github/issues/russell-henderson/repo.svg)](issues)
[![Stars](https://img.shields.io/github/stars/russell-henderson/repo.svg)](stargazers)

### Python Scripts with Descriptions

1. [Disk Analyzer](@disk-analyzer) - Analyzes disk usage and provides a summary of space consumed by files and directories.
2. [Directory Health Analyzer](@directory-health-analyzer) - Analyzes the health of a directory and provides a breakdown of file types.
3. [URL Extractor](@URL-Extractor-Script) - Scrapes data from websites and saves it in a structured format (e.g., CSV, JSON).
4. [System Info](@System-Info-Script) - Scrapes data from websites and saves it in a structured format (e.g., CSV, JSON).
5. [List Directory Files](#list-directory-files) - Scrapes data from websites and saves it in a structured format (e.g., CSV, JSON).
6. [Terminal_Fractal_Explorer](@terminal_fractal_explorer) - Mandelbrot + Julia (color, pan, zoom, save, record).
7. [Convert png to ico](@convert_png_to_ico) - Mandelbrot + PNG to ICO converter.
8. [File Maintenance](@file_maintenance) - Designed to help organize files in a target folder.
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
![Project Image](https://i.ibb.co/8n593Z39/analyze.jpg)
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
![Project Image](https://i.ibb.co/qYD5HTB7/Albedo-Base-XL-A-simple-Python-script-that-extracts-all-URLs-fr-3.jpg)
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

---
![Project Image](https://i.ibb.co/zHfqCfL9/disk.jpg)
## System Info Script

This Python script provides comprehensive information about your system's critical statistics and components. It gathers data on the operating system, CPU, memory, disk usage, and network interfaces, and offers suggestions for improving system performance. The script displays the information in a user-friendly table format, exports the data to a CSV file, and generates a graphical representation of resource usage.

## Features

- **System Information**: Retrieves and displays critical information about the operating system, CPU, RAM, and disk usage.
- **Performance Suggestions**: Provides actionable recommendations for optimizing system performance.
- **Data Export**: Exports the gathered system information to a CSV file for easy reference.
- **Graphical Representation**: Generates a bar chart to visualize CPU usage, RAM used, and disk usage.

## Requirements

To run the script, you will need Python 3.x and the following libraries:

- `psutil`: For gathering system information.
- `pandas`: For handling data and exporting to CSV.
- `matplotlib`: For creating graphical representations.

You can install the required libraries using pip:

```bash
pip install psutil pandas matplotlib
```

## Usage

1. **Download the Script**: Save the script to a file named `system_info.py`.

2. **Run the Script**: Execute the script using Python:

   ```bash
   python system_info.py
   ```

3. **View Output**: The script will output system information to the console, export the data to a file named `system_info.csv`, and generate a bar chart saved as `system_usage.png`.

## Output

- **Console Output**: The system information will be printed in a table format.
- **CSV File**: A file named `system_info.csv` will be created in the same directory as the script, containing the system information.
- **Graph Image**: A bar chart image named `system_usage.png` will be generated to visualize CPU, RAM, and disk usage.

## Performance Suggestions

The script analyzes the system stats and provides suggestions based on:

- Available RAM
- Disk usage percentage
- CPU usage percentage
- RAM usage relative to total RAM

## Example Output

```
--- System Information ---
          Component                Value
              OS                   Linux
         OS Version           5.4.0-42-generic
          OS Release                 5.4.0
       Architecture              64bit
          Hostname              your-hostname
         IP Address              192.168.1.2
        CPU Cores                  4
      CPU Usage (%)              35.5
    RAM Total (GB)                15.0
  RAM Available (GB)              10.5
      RAM Used (GB)                 4.5
    Disk Usage (%)                  65
    Disk Total (GB)                500
      Disk Used (GB)               325
      Disk Free (GB)               175

--- Performance Suggestions ---
- Your CPU is under heavy load. Check for resource-heavy applications.
```

### Customization

You can customize the script by adding additional metrics or modifying the performance suggestions based on your specific needs. The script is designed to be easily extensible.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Acknowledgements

- This script utilizes the `psutil`, `pandas`, and `matplotlib` libraries, which are open-source and widely used in the Python community for system monitoring and data visualization.

### Contributing

Contributions are welcome! If you have suggestions for improvements or additional features, feel free to create an issue or pull request.


---

![Project Image](https://i.ibb.co/zHfqCfL9/disk.jpg)
## List Directory Files

## Overview

`list_files.py` is a Python script that generates a text file containing the hierarchical structure of files and directories starting from a specified directory. The output is formatted in a tree structure, making it easy to visualize the organization of files and folders.

## Features

- Recursively lists all files and folders in the specified directory.
- Outputs the directory structure in a readable tree format.
- Default directory is set to `E:\_women`, but can be modified to any valid directory path.
- Creates a text file named `file_structure.txt` in the same directory as the script.

## Requirements

- Python 3.x installed on your machine.
- Basic knowledge of running scripts in a command line interface.

## Installation

1. **Download Python**: If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/) and install it.

2. **Download the Script**: Copy the `list_files.py` script and save it to your preferred directory.

### Usage

1. **Open Command Prompt or Terminal**:
   - Navigate to the directory where you saved `list_files.py`.

2. **Run the Script**:
   - Execute the script by typing the following command:
     ```bash
     python list_files.py
     ```

3. **Output**:
   - After running the script, it will create a file named `file_structure.txt` in the same directory where the script is located.
   - The `file_structure.txt` will contain the tree structure of the specified directory (`E:\_women` by default).

4. **Change the Default Directory**:
   - To change the directory from which to list files, modify the `directory` variable in the script:
     ```python
     directory = r"E:\_women"  # Change this to your desired directory path
     ```

### Example Output

If the directory structure of `E:\_women` is as follows:

```
E:\_women
    /sub_dir
        file1.txt
        file2.txt
    file3.txt
```

The content of `file_structure.txt` will be:

```
_women/
    sub_dir/
        file1.txt
        file2.txt
    file3.txt
```

### Error Handling

- If the specified directory does not exist, the script will output an error message:
  ```
  The specified path is not a valid directory. Please check the path and try again.
  ```

### Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to create a pull request or open an issue.

### License

This project is open-source and available under the [MIT License](LICENSE).

---
<img src="https://i.ibb.co/5h7BZWrm/Albedo-Base-XL-a-gta5-inspired-coder-style-avatar-with-a-cool-a-3.jpg" 
     alt="BIO" 
     width="300" 
     style="box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.7);">


## ✨ Connect with Me

I'm always open to discussions and collaborations! Feel free to reach out through any of the platforms below:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0e76a8?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/russelllhenderson)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=flat&logo=twitter&logoColor=white)](https://twitter.com/rusty_dallas)
[![Instagram](https://img.shields.io/badge/Instagram-D50032?style=flat&logo=instagram&logoColor=white)](https://www.instagram.com/rhendersonnft/)
[![Discord](https://img.shields.io/badge/Discord-7289DA?style=flat&logo=discord&logoColor=white)](https://discord.gg/FNvb5ECEd8)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/russell-henderson)
[![Telegram](https://img.shields.io/badge/Telegram-0088CC?style=flat&logo=telegram&logoColor=white)](https://t.me/@hexbutt)
[![TikTok](https://img.shields.io/badge/TikTok-000000?style=flat&logo=tiktok&logoColor=white)](https://www.tiktok.com/@rustycalifornia)

## 🌍 Support My Work

If you appreciate my work and would like to support my contributions, consider donating to one of the following organizations:

- [SurfRider Foundation](https://www.surfrider.org)
- [Amnesty International](https://www.amnesty.org)
- [Doctors Without Borders](https://www.doctorswithoutborders.org)
- [HG Blockchain Development](https://www.linkedin.com/company/hg-dev/)

## 📧 Contact Information

For inquiries, please email me at: [russellhenderson@my.unt.edu](mailto:russellhenderson@my.unt.edu)

---

<div style="text-align: center;">
  <small>© 2025 Russell Henderson. Share, rip, improve and enhance.</small>
</div>
