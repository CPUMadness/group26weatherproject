
#
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://i.imgur.com/OrUTyrN.png">
  <source media="(prefers-color-scheme: light)" srcset="https://i.imgur.com/DD2HkFX.png">
</picture>


# Requirements
1. Python 3.12 or newer installed



# Local Deployment Instructions (Windows)
## Step 1: Download
1. Download the .zip of this repository from GitHub.
2. Unzip the file in your desired directory.

## Step 2: Enter API key
1. Acquire an API key at https://openweathermap.org/api
2. In ``.\weatherapp\views.py``, change ``'REPLACE_THIS_WITH_YOUR_OWN_KEY'`` with your API key.
3. In ``.\group26_project\settings.py``, change ``'REPLACE_THIS_WITH_YOUR_OWN_KEY'`` with your own secret key.

## Step 3: Initialize a Python virtual environment
1. **py -m venv .venv**
 *This will create a virtual environment folder titled ".venv" in the projects directory.*
 2.  **.venv\Scripts\activate**
 *This turns on the virtual environment.*
 
 ## Step 4: Starting the project
 1. In Command Prompt, enter:
 ```
 pip install -r requirements.txt
 py manage.py migrate
 py manage.py createsuperuser
 py manage.py runserver 
 ```

## Step 5: Access the website
If you see on Command Prompt
``` Performing system checks...
System check identified no issues (0 silenced).
April 11, 2025 - 15:14:33
Django version 5.2, using settings 'group26_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK. 
``` 
The website is working and listening on Port 8000. This site  can be accessed at 127.0.0.1:8000 or localhost:8000
 


# Pythonanywhere Deployment Instructions
## Step 1: Create an account on [pythonanywhere.com](https://www.pythonanywhere.com).
## Step 2: Download and Upload the Project's Files
1. Download the entire repo from this github.
2. On Pythonanywhere, go to Files > Upload a file, and select the downloaded zip file.
3. Go to Consoles > Bash and enter 'unzip group26_project'.
## Step 3: Create the Web App
1. Go to Web > add a new web app.
2. Choose manual configuration.
3. Select Python 3.10.
## Step 4: Configure the Web App
1. Go to Web and click the newly created web app.
2. Scroll down to WSGI configuration file and click to edit.
3. Replace the content with:
   
```python
import sys
import os

# Update the path to your project folder
path = '/home/yourusername/group26_project'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'group26_project.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

```
4. Replace `yourusername` with your pythonanywhere username
## Step 5: Set Variables
1. In group26_project/settings.py, set `DEBUG = False` and update the `SECRET_KEY`.
3. Add the pythonanywhere domain to `ALLOWED_HOSTS`.

   `ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']`
4. In group26_project/weatherapp/views.py, replace the `API_KEY` with your own OpenWeather API key.

## Step 6: Migrate and Superuser
1. Open the bash console and enter:
```bash
cd group26_project
python manage.py migrate
python manage.py createsuperuser
```
## Step 7: Reload the Web App!
The app should be live and fully functional now!
   
# AI Citation
We used ChatGPT o3-mini-high to generate the basic outline code of our project. It created the basic pages of our project with working algorithms for the sign in. login, and api requests, that we edited to fit our needs. The prompt used was the text of our project proposal + "create the code outline of this project". All files were affected.
# group26weatherproject
Group 26 Weather Project


# Pythonanywhere Deployment Instructions
## Step 1: Create an account on [pythonanywhere.com](https://www.pythonanywhere.com).
## Step 2: Download and Upload the Project's Files
1. Download the entire repo from this github.
2. On Pythonanywhere, go to Files > Upload a file, and select the downloaded zip file.
3. Go to Consoles > Bash and enter 'unzip group26_project'.
## Step 3: Create the Web App
1. Go to Web > add a new web app.
2. Choose manual configuration.
3. Select Python 3.10.
## Step 4: Configure the Web App
1. Go to Web and click the newly created web app.
2. Scroll down to WSGI configuration file and click to edit.
3. Replace the content with:
   
```python
import sys
import os

# Update the path to your project folder
path = '/home/yourusername/group26_project'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'group26_project.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

```
4. Replace `yourusername` with your pythonanywhere username
## Step 5: Set Variables
1. In group26_project/settings.py, set `DEBUG = False` and update the `SECRET_KEY`.
3. Add the pythonanywhere domain to `ALLOWED_HOSTS`.

   `ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']`
4. In group26_project/weatherapp/views.py, replace the `API_KEY` with your own OpenWeather API key.

## Step 6: Migrate and Superuser
1. Open the bash console and enter:
```bash
cd group26_project
python manage.py migrate
python manage.py createsuperuser
```
## Step 7: Reload the Web App!
The app should be live and fully functional now!
   
# AI Citation
We used ChatGPT o3-mini-high to generate the basic outline code of our project. It created the basic pages of our project with working algorithms for the sign in. login, and api requests, that we edited to fit our needs. The prompt used was the text of our project proposal + "create the code outline of this project". All files were affected.
