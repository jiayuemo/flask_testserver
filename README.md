# flask_testserver
Quick Flask Web Application that serves static html pages
## Project Description
Python Flask Web Application that servers static HTML.
Each HTML page includes links to the other pages of the web application.
Created to be able to test out Web Crawler Project.
## Startup Instructions
### Project Setup
You can skip this section if are familiar with Python, venv, and pip.
#### Python
Have Python 3 installed on your machine. https://www.python.org/downloads/
#### Python Virtual Environment (venv)
Venv allows you to use a python virtual environment and install project specific dependencies.
Instead of having a global python runtime with different dependencies supporting many projects
you use an environment where only the bare basics are needed.
See the documentation for venv here: https://docs.python.org/3.6/library/venv.html#module-venv
#### Python Package Manager, PIP
Pip is how python downloads, updates and manages python packages and dependencies.
See the documentation here: https://docs.python.org/3/installing/index.html
### Running the application
Navigate to the directory containing the source code. Then run this command to install project dependencies.
'''
pip install requirements.txt
'''
Once dependencies are installed, you can start the web application with this command.
'''
python simplewebserver.py
'''
If you look to the console, flask will tell you which address and port you can navigate to the project.
