# FlaskTracker

FlaskTracker is a simple web-application program using the Flask
framework.  This application can be used to create a user, who is
able to view locations that are available in the La Grande, OR
area. A user may select one of these locations as a location that
they have recently visited, which will add their data to the app.
From there, the user may choose to generate a report of their data
from a separate web page. This report will contain the percent 
chance that a user might be infected, based on other users,
who may have been infected which also (previously) visited the
same location.  If the user is identified as having a high or 
assured percentage of infection, they may choose to generate a
path that shows where they were most likely to have become
infected.


## Developers
* Ethan Pitzer, pitzere@eou.edu, pitzer-e
* Dan Hughes, dthughes@eou.edu, DanTheFisherman
* Noah Chaney, njchaney@eou.edu, njchaney
* Steve Wilkins, swilkins@eou.edu, imminent-darkness

## Usage

## Updates

This section intends to provide the reader with a more detailed
explanation of the underlying updates which were included in a 
given update. Throughout the development process, updated code
will be pushed to our Git repository, which will include a small
description of the update which was included.

<i> As of 2021-05-25, the updates will adhere the following 
format: </i> <br>
<i>year-month-day, summary of update</i>


### 2021-05-18, Initial Git Commit

The initial commit saw the creation of the Git repository. The
FlaskTracker project includes all necessary libraries and
packages for the application to function.  The initial HTML files
were created for the project using BootStrap templates, and a
simple .py file was created for app definition and imports. -Ethan

### 2021-05-19, New HTML & Documentation

The updated code pushed to Git VCS on 2021-05-19 included a new
HTML page titled 'report.html' which is intended to serve as the
web-page responsible for hosting and serving report generation
functionality. Additional documentation was added to better 
document code changes going forward. -Ethan

### 2021-05-24, Page Naming & Small Updates

This update was rather minor. The 'location.html' page was changed
to be renamed to 'data.html', along with renaming in the
appropriate areas throughout the project document. A small change
in the vcs.xml document was included, having made a small change
to the content formatting. <br><br> <b>It is important to note that there
was one large change to the working Git file. While nothing has
changed regarding filename, a new repository was created which has
a new build-hierarchy.</b><br><br> Because of this, an updated link
to the new repository was sent out to teammates on 2021-05-24 to
ensure continued and updated access to the working project
repository. The rebuild is intended to allow for better linked
Git updates to the remote-Git repository location via commit/push
actions through local IDE's (i.e, PyCharm). -Ethan

### 2021-05-25, Updated Libraries and SQLAlchemy

This was a large and vital update for the FlaskTracker project. The virtual
environment directory was updated to include the flask-sqlalchemy library, so
that the SQLAlchemy object could be called during the creation of the SQLite3
database. Additionally, in order to accommodate this, the virtual environment
needed to reflect changes to the underlying python libraries. Python 2.7 was
retired in January 2021, and as such, no longer included updates to the flask
sqlalchemy packages. <br><br><b>Because of this, pip3 (Python3 package handler) was
used to re-package the underlying python dependencies so that the latest
(currently 3.9) Python development environment can be used.</b><br><br>
Following this Python update, the latest flask-sqlalchemy libraries were
packaged and included into this update of FlaskTracker.  A new HTML5 file
was created 'base.html', which is to be used as the extended template for
other HTML pages to include. This helps create a more modular environment,
and allows for cleaner web-side development. Jinja2 templating has begun
inclusion at this point of development, and was used to provide url linking
to the var_bar tables for maneuvering throughout the website. -Ethan