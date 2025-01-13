#Kunal Sharma IIT Jammu
#2023UMA0221
#Mathematics and Computing

import csv
from urllib.parse import urlparse

def sort_csv_by_domain(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            header = next(reader)
            rows = list(reader)

        unique_urls = list(set(row[0] for row in rows))
        sorted_urls = sorted(unique_urls, key=lambda url: urlparse(url).netloc)

        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(header)
            for url in sorted_urls:
                writer.writerow([url])

        print(f"Sorted links by domain saved to {output_file}")
    except Exception as e:
        print(f"Error sorting CSV by domain: {e}")


def main():
    input_csv = 'final_links.csv'
    output_csv = 'sorted_final_links.csv'
    sort_csv_by_domain(input_csv, output_csv)


if __name__ == '__main__':
    main()