from flask import Flask, render_template, send_file

# Initialize Flask app
app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
