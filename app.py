import streamlit as st
import os


def get_image_path(image_name):
    image_path = os.path.join('images', image_name)
    return image_path


def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# Data
resume_data = {
    'name': 'Dhiman Ghosh',
    'title': 'Senior Software Developer',
    'sub_title': 'Bosch Global Software Technologies',
    'email': 'dgkiitcsedual@gmail.com',
    'phone1': '+91-7975924877',
    'phone2': '+91-8093869430',
    'about_me': 'I am passionate about Software Product Development and working in automation and productivity \
                improvement-focused software product development initiatives at Bosch. \
                I am currently developing software products using Python3 for multiple Bosch home appliances. \
                I have worked on various automation projects. Even worked on an automatic code generator for multiple products.',
    'linkedin': 'https://www.linkedin.com/in/dhiman-ghosh-05a594b2/',
    'github': 'https://github.com/DhimanGhosh',
    'education': {
        '10th': 'ICSE, 2010',
        '12th': 'ISC, 2012',
        'University': 'B.Tech. in Computer Science, 2012 - 2016'
    },
    'work_history': [
        {
            'position': 'Senior Engineer',
            'employer': 'Bosch Global Software Technologies',
            'duration': 'Mar 2022 - Present',
            'projects': [
                {
                    'name': 'Automatic Code Generator Tool',
                    'description_points': (
                        'Developed a tool with user base of ~500 that can automatically generate python \
                        code based on specific input format to improve development productivity by 80%',
                        'These generated python adapter files provides various APIs used for communicating \
                        with the lower layer embedded hardware via TCP/Websocket communication'
                    ),
                    'technologies': 'Python, Jinja2'
                },
                {
                    'name': 'Embedded Adapter Communication Tools',
                    'description_points': (
                        'Desktop Bus: Developed a tool that provides APIs to communicate with \
                        hardware which supports only bus communication on Linux environment',
                        'Secure Shell: Developed a tool based on Paramiko to communicate with \
                        hardware using SSH protocol that provides various APIs that can inject \
                        files/directories and read files/directories to and from the hardware capable of SSH communication',
                        'These tools helps in interacting with the hardware for diagnostic, monitoring and debugging purposes with user base of >1000'
                    ),
                    'technologies': 'Python, dbus-python, paramiko'
                }
            ]
        },
        {
            'position': 'Module Lead',
            'employer': 'Mindtree Ltd.',
            'duration': 'Oct 2021 - Mar 2022',
            'projects': [],
            'work': 'full stack web application development using Flask and sqlite3'
        },
        {
            'position': 'SDET',
            'employer': 'Zebra Technologies',
            'duration': 'Mar 2020 - Oct 2021',
            'projects': [],
            'work': 'Automation Testing using Pytest for Android based scanners'
        },
        {
            'position': 'Technology Analyst',
            'employer': 'Infosys Ltd.',
            'duration': 'Jul 2016 - Feb 2020',
            'projects': [],
            'work': 'Automation Testing using Pytest for blade server'
        }
    ],
    'projects': [
        {
            'name': 'Resume Dashboard',
            'description': 'Webpage of my resume with streamlit',
            'technologies': 'Python, streamlit, html, css',
            'link': 'https://github.com/DhimanGhosh/Resume_Dashboard'
        },
        {
            'name': 'File Server Client',
            'description': 'Python implementation of client server file download program in which the server sends a file to the client',
            'technologies': 'Python, BeautifulSoup',
            'link': 'https://github.com/DhimanGhosh/File_Server_Client'
        },
        {
            'name': 'Smart Door Bell',
            'description': 'Simple Hand Wave Door Bell with Raspberry Pi',
            'technologies': 'Python, RaspberryPi',
            'link': 'https://github.com/DhimanGhosh/Smart_Door_Bell'
        }
    ],
    'skills': {
        'python': 5,
        'flask': 4,
        'SQL': 3,
        'pandas': 3,
        'numpy': 3,
        'matplotlib': 3,
        'seaborn': 3,
        'sklearn': 2,
        'EDA': 3,
        'jira': 4,
        'jenkins': 4,
        'pytest': 4,
        'git': 5,
        'github': 5,
        'streamlit': 3
    },
    'certification_achievements': [
        {
            'title': 'Scaler Academy',
            'image_file_name': 'scaler.png',
            'description': 'On going certification course for Data Science and ML'
        },
        {
            'title': 'Group project excellence award at Bosch',
            'image_file_name': 'bosch.png',
            'description': 'Group of 3 people secured 1st place in python project using streamlit, sqlite3, python, pandas, matplotlib'
        }
    ]
}

# Set page configuration
st.set_page_config(page_title="Dhiman Ghosh - Resume Dashboard", page_icon=":page_facing_up:", layout="wide")

# Custom CSS for styling
load_css('static/styles.css')

# Sidebar/Profile Section
with st.sidebar:
    st.image(get_image_path("profile.png"), width=200)
    st.markdown(f"<h1 style='color:skyblue;'>{resume_data['name']}</h1>", unsafe_allow_html=True)
    st.subheader(resume_data['title'])
    st.write(resume_data['sub_title'])

    # Add a download button for the resume
    resume_file_path = "static/resume.pdf"
    with open(resume_file_path, "rb") as file:
        btn = st.download_button(
            label="📥 Download Resume",
            data=file,
            file_name="Dhiman_Ghosh_Resume.pdf",
            mime="application/pdf"
        )

    st.write(f":telephone_receiver: {resume_data['phone1']} | {resume_data['phone2']}")
    st.markdown(f"""
            <div style="text-align: center;">
                <a href="mailto:{resume_data['email']}"><img src="https://img.icons8.com/fluent/48/000000/gmail.png"/></a>
                <a href="{resume_data['linkedin']}"><img src="https://img.icons8.com/fluent/48/000000/linkedin.png"/></a>
                <a href="{resume_data['github']}"><img src="https://img.icons8.com/fluent/48/000000/github.png"/></a>
            </div>
        """, unsafe_allow_html=True)

    st.write('---')
    st.title("Education")
    for institute, education in resume_data['education'].items():
        st.write(f"**{institute}** : {education}")

with st.container():
    about_col, skills_col = st.columns(2)

    with about_col:
        st.header("About")
        st.write(resume_data['about_me'])

        st.header("Work History")
        for work in resume_data['work_history']:
            position = work.get('position', '')
            employer = work.get('employer', '')
            duration = work.get('duration', '')
            projects = work.get('projects', [])
            work = work.get('work', '')

            st.markdown(f"<h4>{duration} :: {employer}</h4>", unsafe_allow_html=True)
            st.markdown(f"<b class='pre_text'>Position:</b> {position}", unsafe_allow_html=True)
            if projects:
                st.markdown(f"<h6>Projects:</h6>", unsafe_allow_html=True)
                for i, project in enumerate(projects):
                    st.markdown(f"<b>Project {i + 1}:</b> {project['name']}", unsafe_allow_html=True)
                    for point in project['description_points']:
                        st.markdown(f"- {point}", unsafe_allow_html=True)
                    st.markdown(f"<b>Technologies:</b> {project['technologies']}", unsafe_allow_html=True)
            elif work:
                st.markdown(f"<b class='pre_text'>Work:</b> {work}", unsafe_allow_html=True)

    with skills_col:
        st.header("Skills")
        # Sort skills by proficiency in descending order
        sorted_skills = sorted(resume_data['skills'].items(), key=lambda x: x[1], reverse=True)

        # Display skills with progress bars
        for skill, level in sorted_skills:
            st.markdown(f"""
                <div id='skills-body'>
                    <div id='skill-bar' style='width: {level * 20}%'>
                        <span id='skill-text'>{skill}</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)

        st.header("Projects")
        for project in resume_data['projects']:
            name = project.get('name')
            description = project.get('description')
            technologies = project.get('technologies')
            link = project.get('link')

            st.markdown(f"<h4>{name}</h4>", unsafe_allow_html=True)
            st.markdown(f"<b>Description:</b> {description}", unsafe_allow_html=True)
            st.markdown(f"<b>Technologies:</b> {technologies}", unsafe_allow_html=True)
            st.markdown(f"<b><a href='{link}'>Project Link</a></b>", unsafe_allow_html=True)

        st.header("Certification & Achievements")
        for item in resume_data['certification_achievements']:
            image_file_name = item.get('image_file_name', '')
            title = item.get('title', '')
            description = item.get('description', '')

            img_col, desc_col = st.columns([1, 3])

            with img_col:
                img = get_image_path(image_file_name)
                st.image(img, width=100)
            with desc_col:
                st.markdown(f"<h4>{title}</h4>", unsafe_allow_html=True)
                st.markdown(f"<p>{description}</p>", unsafe_allow_html=True)
