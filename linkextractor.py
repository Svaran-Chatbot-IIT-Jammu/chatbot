#Kunal Sharma IIT Jammu
#2023UMA0221
#Mathematics and Computing

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import os
from urllib.parse import urlparse, urljoin

driver = webdriver.Chrome()

def save_to_csv(file_name, data):
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["URL"])
        for url in data:
            writer.writerow([url])

def read_from_csv(file_name):
    if not os.path.exists(file_name):
        return []
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        return [row[0] for row in reader]

def extract_links(base_url):
    driver.get(base_url)
    time.sleep(5)

    links = set()
    for anchor in driver.find_elements(By.TAG_NAME, 'a'):
        href = anchor.get_attribute('href')
        if href and href.startswith(base_url):
            links.add(href)

    return list(links)

def main():
    base_url = 'https://iitjammu.ac.in/'
    first_csv = 'initial_links.csv'
    second_csv = 'final_links.csv'

    initial_links = extract_links(base_url)
    save_to_csv(first_csv, list(set(initial_links)))

    visited_links = set()

    for url in read_from_csv(first_csv):
        if url not in visited_links:
            try:
                print(f"Visiting: {url}")
                new_links = extract_links(url)
                visited_links.update(new_links)
            except Exception as e:
                print(f"Error visiting {url}: {e}")

    save_to_csv(second_csv, list(visited_links))

    final_links = list(set(read_from_csv(second_csv)))
    save_to_csv(second_csv, final_links)

    print(f"Initial links saved to {first_csv}")
    print(f"Final links saved to {second_csv}")

if __name__ == '__main__':
    try:
        main()
    finally:
        driver.quit()