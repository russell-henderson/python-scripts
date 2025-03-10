import requests
from bs4 import BeautifulSoup
import csv
import sys


def get_urls_from_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    urls = set()

    for link in soup.find_all('a', href=True):
        href = link.get('href')
        # Make sure to only collect valid URLs
        if href.startswith('http'):
            urls.add(href)

    return urls


def save_urls_to_csv(urls, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for url in urls:
            writer.writerow([url])


def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <output.csv>")
        return

    url_to_analyze = sys.argv[1]
    output_csv = sys.argv[2]

    print(f"Fetching URLs from: {url_to_analyze}")
    urls = get_urls_from_page(url_to_analyze)

    if urls:
        print(f"Found {len(urls)} URLs. Saving to {output_csv}")
        save_urls_to_csv(urls, output_csv)
        print("Done.")
    else:
        print("No URLs found.")


if __name__ == "__main__":
    main()
