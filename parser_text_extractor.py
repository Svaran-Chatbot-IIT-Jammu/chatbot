#Kunal Sharma IIT Jammu
#2023UMA0221
#Mathematics and Computing

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import csv
import os

driver = webdriver.Chrome()

def read_from_csv(file_name):
    if not os.path.exists(file_name):
        return []
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        return [row[0] for row in reader]

def save_extracted_data(file_name, data):
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["URL", "Extracted Text"])
        for url, text in data.items():
            writer.writerow([url, text])

def extract_text_from_page(url):
    driver.get(url)
    time.sleep(5)
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text(separator=' ', strip=True)

def main():
    input_csv = 'sorted_final_links.csv'
    output_csv = 'extracted_text.csv'

    urls = read_from_csv(input_csv)
    extracted_data = {}

    for url in urls:
        try:
            print(f"Processing: {url}")
            text_data = extract_text_from_page(url)
            extracted_data[url] = text_data
        except Exception as e:
            print(f"Error processing {url}: {e}")

    save_extracted_data(output_csv, extracted_data)
    print(f"Extracted text data saved to {output_csv}")

if __name__ == '__main__':
    try:
        main()
    finally:
        driver.quit()
