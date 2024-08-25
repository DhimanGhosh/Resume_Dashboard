import os
import threading
import time
import requests
from flask import Flask, render_template, send_file
from flask.cli import AppGroup
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Initialize Flask app
app = Flask(__name__)
collect_cli = AppGroup('collect', help='Collect static files')


@collect_cli.command('static')
def collect_static():
    """Collect static files."""
    print("Collecting static files...")  # Placeholder for actual collection logic


@app.route('/')
def resume():
    """Render the resume page."""
    resume_data = {
        'name': 'Dhiman Ghosh',
        'title': 'Senior Software Developer',
        'sub_title': 'Bosch Global Software Technologies',
        'email': 'dgkiitcsedual@gmail.com',
        'phone': '+91-7975924877',
        'linkedin': 'https://www.linkedin.com/in/dhiman-ghosh-05a594b2/',
        'github': 'https://github.com/DhimanGhosh',
        'experience': [
            ('Senior Software Developer', 'Bosch Global Software Technologies'),
            ('Software Engineer', 'Mindtree Ltd.'),
            ('SDET', 'Zebra Technologies'),
            ('System Engineer', 'Infosys Ltd.')
        ],
        'qualifications': [
            'B.Tech. in Computer Science',
            '7.5 years of industry experience'
        ],
        'work_history': [
            {
                'position': 'Senior Developer',
                'company': 'Tech Corp',
                'duration': 'Jan 2020 - Present',
                'description': 'Leading a team to develop scalable web applications.'
            },
            {
                'position': 'Developer',
                'company': 'Web Solutions',
                'duration': 'Jan 2018 - Dec 2019',
                'description': 'Worked on various client projects to build web applications.'
            }
        ],
        'projects': [
            {
                'name': 'Project A',
                'description': 'Developed an e-commerce platform with real-time analytics.',
                'technologies': 'Python, Django, JavaScript'
            },
            {
                'name': 'Project B',
                'description': 'Created a mobile app for social networking.',
                'technologies': 'Flutter, Firebase'
            }
        ],
        'skills': {
            'python': 5,
            'flask': 4,
            'SQL': 3,
            'pandas': 3,
            'numpy': 3,
            'matplotlib': 3,
            'sklearn': 2,
            'jira': 4,
            'jenkins': 4,
            'pytest': 4,
            'git': 5,
            'github': 5
        }
    }
    return render_template('resume.html', **resume_data)


@app.route('/download_resume')
def download_resume():
    """Serve the resume file for download."""
    return send_file('static/Dhiman_Resume.pdf', as_attachment=True)


# Define the Flask app host and port
base_url = 'http://127.0.0.1:5000'
output_dir = 'static_site'

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


def save_file(url, path):
    """Save a file from the given URL to the specified path."""
    # Ensure that the directory exists
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # Download and save the file
    response = requests.get(url)
    if response.status_code == 200:
        with open(path, 'wb') as file:
            file.write(response.content)
    else:
        print(f"Failed to download {url}")


def scrape_page(url, output_dir):
    """Scrape the page and save the HTML, CSS, and JS files."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Save HTML file
    parsed_url = urlparse(url)
    path = os.path.join(output_dir, parsed_url.path.lstrip('/'))
    if not path.endswith('.html'):
        path = os.path.join(path, 'index.html')
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, 'w', encoding='utf-8') as file:
        file.write(soup.prettify())

    # Save CSS and JS files
    for tag in soup.find_all(['link', 'script']):
        if tag.name == 'link' and tag.get('href'):
            resource_url = urljoin(base_url, tag['href'])
            resource_path = os.path.join(output_dir, urlparse(resource_url).path.lstrip('/'))
            save_file(resource_url, resource_path)
        elif tag.name == 'script' and tag.get('src'):
            resource_url = urljoin(base_url, tag['src'])
            resource_path = os.path.join(output_dir, urlparse(resource_url).path.lstrip('/'))
            save_file(resource_url, resource_path)


def run_flask():
    """Run the Flask app in a separate thread."""
    app.run(debug=False, use_reloader=False)


def main():
    """Main function to run Flask and scrape the site."""
    # Start the Flask app in a separate thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # Wait for the Flask app to start
    time.sleep(2)  # Adjust the sleep time if necessary

    # Scrape the main page
    scrape_page(base_url, output_dir)

    # You can add more URLs to scrape if needed
    # Example: scrape_page(base_url + '/another_page', output_dir)


if __name__ == '__main__':
    # Add CLI command
    app.cli.add_command(collect_cli)
    main()
