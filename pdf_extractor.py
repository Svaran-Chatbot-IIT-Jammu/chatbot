#Kunal Sharma IIT Jammu
#2023UMA0221
#Mathematics and Computing

import os
import csv
import requests
from urllib.parse import urlparse

def read_from_csv(file_name):
    if not os.path.exists(file_name):
        return []
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        return [row[0] for row in reader]

def download_pdf(url, output_folder):
    try:
        response = requests.get(url, stream=True, timeout=10)
        if response.headers.get('Content-Type') == 'application/pdf':
            parsed_url = urlparse(url)
            pdf_name = os.path.basename(parsed_url.path) or 'downloaded.pdf'
            output_path = os.path.join(output_folder, pdf_name)

            with open(output_path, 'wb') as pdf_file:
                for chunk in response.iter_content(chunk_size=1024):
                    pdf_file.write(chunk)

            print(f"Downloaded: {url} to {output_path}")
        else:
            print(f"Skipped (not a PDF): {url}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

def main():
    input_csv = 'sorted_final_links.csv'
    output_folder = 'downloaded_pdfs'

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    urls = read_from_csv(input_csv)

    for url in urls:
        if url.endswith('.pdf'):
            download_pdf(url, output_folder)

    print(f"PDF download process completed. Files saved in '{output_folder}'")

if __name__ == '__main__':
    main()