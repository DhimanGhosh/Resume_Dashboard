import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Configuration
base_url = 'http://127.0.0.1:5000'
output_dir = 'static_site'

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def save_file(url, path):
    response = requests.get(url)
    with open(path, 'wb') as file:
        file.write(response.content)

def scrape_page(url, output_dir):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Save HTML file
    path = os.path.join(output_dir, urlparse(url).path.lstrip('/'))
    if not path.endswith('.html'):
        path += '.html'
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as file:
        file.write(soup.prettify())

    # Save CSS and JS files
    for tag in soup.find_all(['link', 'script']):
        if tag.name == 'link' and tag.get('href'):
            resource_url = urljoin(base_url, tag['href'])
            resource_path = os.path.join(output_dir, urlparse(resource_url).path.lstrip('/'))
            if not resource_path.endswith('.css'):
                resource_path += '.css'
            save_file(resource_url, resource_path)
        elif tag.name == 'script' and tag.get('src'):
            resource_url = urljoin(base_url, tag['src'])
            resource_path = os.path.join(output_dir, urlparse(resource_url).path.lstrip('/'))
            if not resource_path.endswith('.js'):
                resource_path += '.js'
            save_file(resource_url, resource_path)

def main():
    scrape_page(base_url, output_dir)

if __name__ == '__main__':
    main()
