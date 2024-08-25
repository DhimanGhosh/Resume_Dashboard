from flask import Flask, render_template, send_file

app = Flask(__name__)


@app.route('/')
def resume():
    """
    Route handler for the home page.

    This function retrieves resume data and renders the 'resume.html' template
    with the resume data.

    Returns:
        A rendered template with the resume data.
    """
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
    """
    Route handler for downloading the resume.

    Returns:
        A file to be downloaded by the user.
    """
    return send_file('static/Dhiman_Resume.pdf', as_attachment=True)


@app.errorhandler(404)
def page_not_found(e):
    """
    Handles HTTP 404 errors by rendering the '404.html' template and returning a 404 status code.

    Parameters:
        e (Exception): The exception that triggered the error handler.

    Returns:
        tuple: A tuple containing the rendered template and the HTTP status code.
    """
    return render_template('404.html', error=str(e)), 404


if __name__ == '__main__':  # Check if this script is being run directly (not imported)
    app.run(
        debug=True,  # Enable debug mode for the application
        host='0.0.0.0'  # Allow the application to be accessed from any network
    )
