# <center><img src="static/images/family.png" width="20%" alt="FamilyTies"></center> 
# <center><strong>FAMILY TIES</strong></center>


## About Me
Before studying at Hackbright Academy, Quanisha has 10+ years of working experience in food service, sales, healthcare and IT industries combined. Quanisha has always had a love for technology and learning new things. In 2011, she received her Bachelor of Arts (B.A.) degree in Computer Science from University of North Carolina at Charlotte. Recently in 2020, she received her CompTIA A+ and Google IT certifications.



## Contents
* [Tech Stack](#tech-stack)
* [Features](#features)
* [Future State](#future)
* [Installation](#installation)


## <a name="tech-stack"></a>Technologies
* Python
* Flask
* Jinja2
* PostgresQL
* SQLAlchemy ORM
* Javascript
* HTML
* CSS
* Bootstrap
* Cloudinary
* FullCalendar

## <a name="features"></a>Features

## <a name="future"></a>Future State

## <a name="installation"></a>Installation
To run Family Ties on your own machine:

Clone this repo:
```
https://github.com/Quanisha704/Software-Engineering-Project.git
```

Create and activate a virtual environment inside your Family Ties directory:
```
virtualenv env (Mac OS)
virtualenv env --always-copy (Windows OS)
source env/bin/activate
```

Install the dependencies:
```
pip3 install -r requirements.txt
```

Sign up to use the [Google Calendar API](https://developers.google.com/calendar/)

Save your API keys in a file called <kbd>secrets.sh</kbd> using this format:

```
export GOOGLE_API_KEY="YOUR_KEY_HERE"
export GOOGLE_CLIENT_ID="YOUR_ID_HERE"
```

Set up and download your Google OAuth 2.0 client IDs, and save to a file called <kbd>client_secrets.json</kbd>.

Source your keys from your secrets.sh file into your virtual environment:

```
source secrets.sh
```

Set up the database:

```
createdb jobs
python3.6 model.py
python3.6 seed.py
```

Run the app:

```
python3.6 server.py
```

You can now navigate to 'localhost:5000/' to access JobTracker.


